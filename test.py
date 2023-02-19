import os
import time
import requests
import logging
import sys
from dotenv import load_dotenv
import telegram
from exceptions import TypeError, AssertionError, APInotaswer, TokenNotExist

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

# response = {'homeworks': [{'id': 637920, 'status': 'approved', 'homework_name': 'nir0k__hw05_final.zip', 'reviewer_comment': 'Принято!', 'date_updated': '2023-01-25T14:52:15Z', 'lesson_name': 'Проект спринта: подписки на авторов'}, {'id': 620425, 'status': 'approved', 'homework_name': 'nir0k__hw04_tests.zip', 'reviewer_comment': 'Принято!', 'date_updated': '2023-01-16T07:59:43Z', 'lesson_name': 'Проект спринта: покрытие тестами'}, {'id': 599488, 'status': 'approved', 'homework_name': 'nir0k__hw03_forms.zip', 'reviewer_comment': 'Принято!', 'date_updated': '2022-12-28T15:52:50Z', 'lesson_name': 'Проект спринта: новые записи'}, {'id': 527997, 'status': 'approved', 'homework_name': 'nir0k__hw02_community.zip', 'reviewer_comment': 'Принято, отличная работа!', 'date_updated': '2022-11-13T14:46:26Z', 'lesson_name': 'Проект спринта: сообщества'}, {'id': 480095, 'status': 'approved', 'homework_name': 'nir0k__hw_python_oop.zip', 'reviewer_comment': 'Хорошая работа! Оставил пару комментариев, что можно сделать лучше :)', 'date_updated': '2022-10-07T11:36:39Z', 'lesson_name': 'Проект спринта: модуль фитнес-трекера'}], 'current_date': 1676820628}
# response = [{'homeworks': [{'homework_name': 'hw123', 'status': 'approved'}], 'current_date': 123246}]
# response = [{'current_date': 123246, 'homeworks': [{'homework_name': 'hw123', 'status': 'approved'}]}]
# response = {'current_date': 123246, 'homeworks': {'homework_name': 'hw123', 'status': 'approved'}}
response = {'homeworks': {'homework_name': 'hw123', 'status': 'approved'}, 'current_date': 123246}

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