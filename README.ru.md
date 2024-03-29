# homework_bot - Телеграм-бот для проверки статуса рецензии на домашние задания

## Выберите язык

- [English](README.md)
- [Русский](README.ru.md)

---

## О проекте
Данный проект представляет собой Телеграм-бота, предназначенного для автоматической проверки статуса рецензий на домашние задания через API и отправки уведомлений в Телеграм, если статус рецензии обновился. Бот помогает студентам и обучающимся оперативно получать информацию о проверке их работ, не заходя на образовательную платформу.

## Основные функции:
- Проверка статуса рецензий: 
    
    Бот регулярно обращается к API образовательной платформы для проверки статусов рецензий на домашние задания.

- Отправка уведомлений: 

    В случае обновления статуса рецензии бот отправляет сообщение в Телеграм-канал или чат с детальной информацией о статусе проверки.

- Настройка интервала проверки: 
    
    - Пользователи могут настроить желаемый интервал проверки статуса рецензий.

## Технологии
- Python
- Библиотеки для работы с Телеграм API
- Библиотеки для работы с внешними API

## Как использовать

### Настройка Телеграм-бота: 

- Для начала работы необходимо создать бота в Телеграм через BotFather и получить токен.
- **Конфигурация проекта**: В файле конфигурации укажите полученный токен и идентификатор вашего Телеграм-канала или чата.
- **Запуск бота**: Запустите бота, и он начнет регулярную проверку статусов рецензий и отправку уведомлений.

## Как запустить проект
1.  Для запуска проекта необходимо выполнить следующие шаги:
    ```sh
    git clone git@github.com:nir0k/homework_bot.git
    cd homework_bot
    ```
2. Создайте и активируйте виртуальное окружение:
    ```sh
    python3 -m venv env
    source env/bin/activate
    ```
3. Установите зависимости:
    ```sh
    python3 -m pip install --upgrade pip
    pip install -r requirements.txt
    ```
4. Укажите токен и chat ID для Telegram Bot и токен для проверки домашнего задания на yandex.practicum в .env
```sh
PRACTICUM_TOKEN=YA_TOKEN
TELEGRAM_TOKEN=TELEGRAM_TOKEN
TELEGRAM_CHAT_ID=TELEGRAM_CHATID
```

5. Запустите бота
```sh
python3 homework.py
```
