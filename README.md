# homework_bot - Telegram Bot for Checking Homework Review Status

## Choose Your Language

- [English](README.md)
- [Русский](README.ru.md)

---

## About the Project
This project is a Telegram bot designed for automatic checking of homework review statuses via API and sending notifications in Telegram if the review status is updated. The bot helps students and learners promptly receive information about the review of their work without having to visit the educational platform.

## Key Features:
- Review Status Check:

    The bot regularly accesses the educational platform's API to check the statuses of homework reviews.

- Sending Notifications:

    If the review status is updated, the bot sends a message in the Telegram channel or chat with detailed information about the review status.

- Checking Interval Setting:

    Users can customize the desired interval for checking review statuses.

## Technologies
- Python
- Libraries for working with Telegram API
- Libraries for working with external APIs

## How to Use
### Setting Up the Telegram Bot:
- To start, you need to create a bot in Telegram via BotFather and obtain a token.
- Project Configuration: In the configuration file, specify the obtained token and the identifier of your Telegram channel or chat.
- Bot Launch: Start the bot, and it will begin regular checks of review statuses and sending notifications.


## How to Run the Project
1. To run the project, follow these steps:

    ```sh
    git clone git@github.com:nir0k/homework_bot.git
    cd homework_bot
    ```

2. Create and activate a virtual environment:

    ```sh
    python3 -m venv env
    source env/bin/activate
    ```

3. Install the dependencies:

    ```sh
    python3 -m pip install --upgrade pip
    pip install -r requirements.txt
    ```

4. Specify the token and chat ID for the Telegram Bot and the token for checking homework on yandex.practicum in .env

    ```sh
    PRACTICUM_TOKEN=YA_TOKEN
    TELEGRAM_TOKEN=TELEGRAM_TOKEN
    TELEGRAM_CHAT_ID=TELEGRAM_CHATID
    ```

5. Start the bot

    ```sh
    python3 homework.py
    ```
