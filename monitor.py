from telethon import TelegramClient, events
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from pygame import mixer
import webbrowser
import time

# Welcome messages
print("Telegram Text Monitor")
print("Author: Mahmud Hasan Saikot")
print("Email: saikath65@gmail.com\n")

# Test mode on/off; for monitoring a test group rather than the actual one
testMode = 'on'

# Group/chat IDs to monitor
regularF1 = ##########
testGroup = ##########

if testMode == 'on':
    chatID = testGroup
    print("Test mode on. Turn it off for monitoring real chat texts.\n")
elif testMode == 'off':
    chatID = regularF1
    print("Monitoring texts for", chatID, "...\n")
else:
    chatID = testGroup
    print("Error: The \"testMode\" variable value can only be set to either \"on\" or \"off\"")

# Trigger words to sound the alarm
trigger1 = 'jun'
trigger2 = 'jul'
trigger3 = 'may'
negTrigger = 'ns'

# Declare alarm path and initiate music player & global variables
# alarmStopppingInterval is the time (s) to check for negative trigger since the alarm starts and
# alarm will be turned off if there is any negative trigger within this time period
pathAlarm = r'Alarm.mp3'
mixer.init()
mixer.music.load(pathAlarm)
alarmState = 0
timeStart = 0
alarmStoppingInterval = 40

# URL to open when triggered
openURL = 'https://example.com/'

# Use your telegram details; retrieving them is easy, create a new API app from https://my.telegram.org/
api_id = 'Your_API_ID'
api_hash = 'Your_API_HASH'
client = TelegramClient('newsess', api_id, api_hash)

# Authenticate and listen to your telegram chat texts
@client.on(events.NewMessage(chats=[chatID]))
async def my_event_handler(event):
    global alarmState
    global timeStart
    txt = event.raw_text
    txtLow = event.raw_text.lower()
    print(txt)
    if (trigger1 in txtLow or trigger2 in txtLow or trigger3 in txtLow) and negTrigger not in txtLow:
        alarmState = 1
        timeStart = time.time()
        print("\n**** Alarm Started! Triggered by <", txtLow, "> ****\n")
        mixer.music.play()
        if testMode == 'off':
            webbrowser.open(openURL)
    if alarmState == 1:
        if time.time() - timeStart < alarmStoppingInterval:
            if negTrigger in txtLow:
                alarmState = 0
                print("\n**** Alarm Stopped! Triggered by <", txtLow, "> ****\n")
                mixer.music.stop()

# Start the client and run until the session expires
client.start()
client.run_until_disconnected()