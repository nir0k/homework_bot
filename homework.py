import os
import time
import requests
import logging
import sys
from dotenv import load_dotenv
import telegram
from exceptions import APInotaswer, TokenNotExist

load_dotenv()

logger = logging.getLogger()
streamHandler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter(
    '%(asctime)s, %(name)s, [%(levelname)s]: %(message)s')
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)

PRACTICUM_TOKEN = os.getenv('PRACTICUM_TOKEN')
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')

RETRY_PERIOD = 600
ENDPOINT = 'https://practicum.yandex.ru/api/user_api/homework_statuses/'
HEADERS = {'Authorization': f'OAuth {PRACTICUM_TOKEN}'}

HOMEWORK_VERDICTS = {
    'approved': 'Работа проверена: ревьюеру всё понравилось. Ура!',
    'reviewing': 'Работа взята на проверку ревьюером.',
    'rejected': 'Работа проверена: у ревьюера есть замечания.'
}


def check_tokens():
    """Check that tokens exists."""
    if not (PRACTICUM_TOKEN or TELEGRAM_TOKEN or TELEGRAM_CHAT_ID):
        message = 'Check tokens. Except mantadory token'
        logger.critical(message)
        raise TokenNotExist(message)


def send_message(bot, message):
    """Send messages into telegram."""
    try:
        bot.send_message(TELEGRAM_CHAT_ID, message)
        logger.debug(f'Сообщение было отправено в Telegram: {message}')
    except Exception as error:
        logger.error(f'Ошибка отправки сообщения в Teegram: {error}')


def get_api_answer(timestamp):
    """Get respnse from api."""
    payload = {'from_date': timestamp}
    try:
        response = requests.get(ENDPOINT, headers=HEADERS, params=payload)
        if response.status_code != 200:
            message = 'Не доступен эндпоинт API Yandex practicum'
            logger.error(message)
            raise APInotaswer(message)
    except requests.RequestException as error:
        logger.error(f'Ошибка при запросе к API Yandex practicum: {error}')
    return response.json()


def check_response(response):
    """Check response and get homeworks."""
    if not isinstance(response, dict):
        message = f'check_response. Wrong answer: {response}'
        logger.error(message)
        raise TypeError(message)
    if 'homeworks' not in response:
        message = "check_response. key homeworks not exist"
        logger.error(message)
        raise TypeError(message)
    if 'current_date' not in response:
        message = "check_response. key current_date not exist"
        logger.error(message)
        raise TypeError(message)
    if not isinstance(response['homeworks'], list):
        message = ('check_response. Wrong type homeworks')
        logger.error(message)
        raise TypeError(message)

    return response['homeworks']


def parse_status(homework):
    """Check status homework."""
    if not homework.get('homework_name'):
        message = "parse_status. homework_name not exist"
        logger.error(message)
        raise AssertionError(message)
    homework_name = homework.get('homework_name')
    if not homework.get('status'):
        message = "parse_status. homework status not exist"
        logger.error(message)
        raise AssertionError(message)
    if not HOMEWORK_VERDICTS.get(homework.get('status')):
        message = "parse_status. homework undefined status"
        logger.error(message)
        raise AssertionError(message)
    verdict = HOMEWORK_VERDICTS[homework['status']]
    return f'Изменился статус проверки работы "{homework_name}". {verdict}'


def main():
    """Основная логика работы бота."""
    check_tokens()
    bot = telegram.Bot(token=TELEGRAM_TOKEN)
    timestamp = int(time.time())
    timestamp = timestamp - (RETRY_PERIOD)
    while True:
        try:
            answer = get_api_answer(timestamp)
            homeworks = check_response(answer)

            for homework in homeworks:
                status = parse_status(homework)
                if status is not None:
                    send_message(bot, status)
                else:
                    logger.debug('No new message')
            timestamp = answer['current_date']
        except Exception as error:
            message = f'Сбой в работе программы: {error}'
            logger.debug(message)
            send_message(bot, message)
        time.sleep(RETRY_PERIOD)


if __name__ == '__main__':
    main()
