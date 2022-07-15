a
# Init The Modules From The Import And Import The Modules
from base64 import decode
from email.header import decode_header
import subprocess
import sys
from pynput.keyboard import Key, Controller
keyboardCon = Controller()
from pynput.mouse import Button, Controller
mouseCon = Controller()
import keyboard
import time
import os
import pyautogui
import urllib.request

# Init Variables
url = "https://themrredstone.github.io/Discord-Spammer-Updater/currentVersion.txt"
width,height = pyautogui.size()
running = True
file = urllib.request.urlopen(url)

with open('settings/version.txt') as f:
    version = f.read()
    print(version)

for line in file:
    newVersion = line.decode("utf-8").strip()
    print(newVersion)
    if newVersion > version:
        print("A New Version Is Available! New Version: v" + newVersion + " Current Version: v" + version)
    else:
        print("Your Up To Date")

os.system("taskkill /f /im Discord.exe")

print("You Are Currently Using Discord Spammer v3.0.0 By Kaden K.")

with open('settings/save.settings') as f:
    contents = f.read()
    print(contents)

if contents:
    print("Your Current Drive Is " + contents)
else:
    drive = input("What Is Your Main Drive? ex: C:/ DO NOT USE \ The Code Wont Work Right \n")
    if drive.__contains__("/"):
        formatedDrive = drive.replace("/", "")
    else:
        formatedDrive = drive

    if os.path.exists(formatedDrive + "/Users"):
        print("EXISTS")
        currentDir = formatedDrive + "/Users/" + os.getlogin() + "/AppData/Local/Discord/"
        print(currentDir)
        file = open("settings/save.settings", "w")
        file.write(currentDir)
        file.close()
    else:
        print("Drive Not Found Ending The Code In 4 Seconds.\nOpen It Again To Retry No Users Folder Found In That Directory")
        time.sleep(4)
        running = False

if running == True:
    SENTENCE = input("How Many Sentences Do You Want To Spam With Limit: 5\n")
    sentenceNum = int(SENTENCE)
    if sentenceNum == 1:
        sentence = input("What Shall The Sentence Say\n")
    elif sentenceNum == 2:
        sentence = input("What Shall The Sentence Say\n")
        sentence2 = input("What Shall The Second Sentence Say\n")
    elif sentenceNum == 3:
        sentence = input("What Shall The Sentence Say\n")
        sentence2 = input("What Shall The Second Sentence Say\n")
        sentence3 = input("What Shall The Third Sentence Say\n")
    elif sentenceNum == 4:
        sentence = input("What Shall The Sentence Say\n")
        sentence2 = input("What Shall The Second Sentence Say\n")
        sentence3 = input("What Shall The Third Sentence Say\n")
        sentence4 = input("What Shall The Fourth Sentence Say\n")
    elif sentenceNum == 5:
        sentence = input("What Shall The Sentence Say\n")
        sentence2 = input("What Shall The Second Sentence Say\n")
        sentence3 = input("What Shall The Third Sentence Say\n")
        sentence4 = input("What Shall The Fourth Sentence Say\n")
        sentence5 = input("What Shall The Fourth Sentence Say\n")
    else:
        running = False
        
    Amount = input("How Many Times Do You Want It To Spam The Sentence\n")
    a = int(Amount)
    print("Press Down Arrow When The Discord App Is Opened In 4 Seconds")

time.sleep(4)

subprocess.Popen(os.path.join(currentDir,"Update.exe --processStart Discord.exe"))
running = True

def spam1():
    for char in sentence:
        if keyboard.is_pressed("escape"):
            print("Closing...")
            sys.exit()
        keyboardCon.press(char)
        if keyboard.is_pressed("escape"):
            print("Closing...")
            sys.exit()
        keyboardCon.release(char)
        if keyboard.is_pressed("escape"):
            print("Closing...")
            sys.exit()
        time.sleep(0.05)
        if keyboard.is_pressed("escape"):
            print("Closing...")
            sys.exit()
    keyboardCon.press(Key.enter)
    if keyboard.is_pressed("escape"):
        print("Closing...")
        sys.exit()
    keyboardCon.release(Key.enter)
    if keyboard.is_pressed("escape"):
        print("Closing...")
        sys.exit()

def spam2():
    for char in sentence2:
        if keyboard.is_pressed("escape"):
            print("Closing...")
            sys.exit()
        keyboardCon.press(char)
        if keyboard.is_pressed("escape"):
            print("Closing...")
            sys.exit()
        keyboardCon.release(char)
        if keyboard.is_pressed("escape"):
            print("Closing...")
            sys.exit()
        time.sleep(0.05)
        if keyboard.is_pressed("escape"):
            print("Closing...")
            sys.exit()
    keyboardCon.press(Key.enter)
    if keyboard.is_pressed("escape"):
        print("Closing...")
        sys.exit()
    keyboardCon.release(Key.enter)
    if keyboard.is_pressed("escape"):
        print("Closing...")
        sys.exit()

def spam3():
    for char in sentence3:
        if keyboard.is_pressed("escape"):
            print("Closing...")
            sys.exit()
        keyboardCon.press(char)
        if keyboard.is_pressed("escape"):
            print("Closing...")
            sys.exit()
        keyboardCon.release(char)
        if keyboard.is_pressed("escape"):
            print("Closing...")
            sys.exit()
        time.sleep(0.05)
        if keyboard.is_pressed("escape"):
            print("Closing...")
            sys.exit()
    keyboardCon.press(Key.enter)
    if keyboard.is_pressed("escape"):
        print("Closing...")
        sys.exit()
    keyboardCon.release(Key.enter)
    if keyboard.is_pressed("escape"):
        print("Closing...")
        sys.exit()

def spam4():
    for char in sentence4:
        if keyboard.is_pressed("escape"):
            print("Closing...")
            sys.exit()
        keyboardCon.press(char)
        if keyboard.is_pressed("escape"):
            print("Closing...")
            sys.exit()
        keyboardCon.release(char)
        if keyboard.is_pressed("escape"):
            print("Closing...")
            sys.exit()
        time.sleep(0.05)
        if keyboard.is_pressed("escape"):
            print("Closing...")
            sys.exit()
    keyboardCon.press(Key.enter)
    if keyboard.is_pressed("escape"):
        print("Closing...")
        sys.exit()
    keyboardCon.release(Key.enter)
    if keyboard.is_pressed("escape"):
        print("Closing...")
        sys.exit()

def spam5():
    for char in sentence5:
        if keyboard.is_pressed("escape"):
            print("Closing...")
            sys.exit()
        keyboardCon.press(char)
        if keyboard.is_pressed("escape"):
            print("Closing...")
            sys.exit()
        keyboardCon.release(char)
        if keyboard.is_pressed("escape"):
            print("Closing...")
            sys.exit()
        time.sleep(0.05)
        if keyboard.is_pressed("escape"):
            print("Closing...")
            sys.exit()
    keyboardCon.press(Key.enter)
    if keyboard.is_pressed("escape"):
        print("Closing...")
        sys.exit()
    keyboardCon.release(Key.enter)
    if keyboard.is_pressed("escape"):
        print("Closing...")
        sys.exit()

# Run The Main Loop
while running:
    # Check If The Button Is Pressed To Disabled The Spammer
    if keyboard.is_pressed('down'):
        print('Spammer Is Activated')
        for i in range(a):
            newI = i = i + 1
            print(str(newI) + " / " + str(a))
            if sentenceNum == 1:
                if keyboard.is_pressed("escape"):
                    print("Closing...")
                    sys.exit()
                spam1()
            elif sentenceNum == 2:
                if keyboard.is_pressed("escape"):
                    print("Closing...")
                    sys.exit()
                spam1()
                if keyboard.is_pressed("escape"):
                    print("Closing...")
                    sys.exit()
                spam2()
                if keyboard.is_pressed("escape"):
                    print("Closing...")
                    sys.exit()
            elif sentenceNum == 3:
                if keyboard.is_pressed("escape"):
                    print("Closing...")
                    sys.exit()
                spam1()
                if keyboard.is_pressed("escape"):
                    print("Closing...")
                    sys.exit()
                spam2()
                if keyboard.is_pressed("escape"):
                    print("Closing...")
                    sys.exit()
                spam3()
                if keyboard.is_pressed("escape"):
                    print("Closing...")
                    sys.exit()
            elif sentenceNum == 4:
                if keyboard.is_pressed("escape"):
                    print("Closing...")
                    sys.exit()
                spam1()
                if keyboard.is_pressed("escape"):
                    print("Closing...")
                    sys.exit()
                spam2()
                if keyboard.is_pressed("escape"):
                    print("Closing...")
                    sys.exit()
                spam3()
                if keyboard.is_pressed("escape"):
                    print("Closing...")
                    sys.exit()
                spam4()
                if keyboard.is_pressed("escape"):
                    print("Closing...")
                    sys.exit()
            elif sentenceNum == 5:
                if keyboard.is_pressed("escape"):
                    print("Closing...")
                    sys.exit()
                spam1()
                if keyboard.is_pressed("escape"):
                    print("Closing...")
                    sys.exit()
                spam2()
                if keyboard.is_pressed("escape"):
                    print("Closing...")
                    sys.exit()
                spam3()
                if keyboard.is_pressed("escape"):
                    print("Closing...")
                    sys.exit()
                spam4()
                if keyboard.is_pressed("escape"):
                    print("Closing...")
                    sys.exit()
                spam5()
                if keyboard.is_pressed("escape"):
                    print("Closing...")
                    sys.exit()

        print("Done! Executing The Code The Spamming Is Finished!")
        os.system("taskkill /f /im Discord.exe")