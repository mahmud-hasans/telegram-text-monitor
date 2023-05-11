# telegram-text-monitor
I created this project to monitor Telegram chat texts and trigger some actions based on specific keywords!

## **IMPORTANT** :red_circle:
1. Specify testMode on/off, Chat IDs, trigger keywords, API credentials, and other variables in **monitor.py** for your use case
2. You might need to disable two factor authentication on your telegram (disable the password)
3. When you run the **monitor.py** file, you will be asked for your phone number and the verification code
4. The telethon package version tested to work in this project is 1.28.5
5. The python version is 3.10 (others should work as well)
6. Chat IDs can be found in many ways. Sometimes if you open telegram in your browser from https://web.telegram.org you will see the Chat ID in the URL bar

## Description
This repository contains a Python code that utilizes the Telegram API to monitor text messages in Telegram groups. 
The code listens for specific keywords within the messages and triggers customized actions when those keywords are detected. 
It provides a flexible framework for performing actions such as raising alarms, opening a web browser with a specific address, or executing any other desired action.

## How to use
To use the code, you will need to provide your own Telegram API credentials: API ID and API hash in the **monitor.py** file. 
These credentials can be obtained by creating an application on the Telegram website (https://my.telegram.org/auth).
Once the credentials are set up, you can specify the chat ID to monitor specific chats, configure trigger keywords, and the corresponding actions to take within the **monitor.py** code.
