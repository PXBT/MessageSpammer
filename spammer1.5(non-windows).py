from time import sleep
import sys
import subprocess
print("Made by Vidhun Nagarajan, 2021")
sleep(0.2)
print("Thanks to SpookySec for original code.")
try:
    import pynput
    print("Pynput library already installed! Skipping installation...")
except ImportError:
    print("Pynput library not installed! Installing...")
    try:
        from pip import main as pipmain
    except ImportError:
        from pip._internal import main as pipmain
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pynput'])
    print("Pynput library has been installed!")
from pynput.mouse import Controller, Button
from pynput import keyboard
from pynput.keyboard import Key
keyboard1 = keyboard.Controller()
mouse = Controller()
input1 = input("Enter what word(s) should be spammed and tap enter:")
spamtime = float(input("Enter time interval (as decimal number, in seconds) between each sent message:"))
spamvalue = int(input("Enter number of times to spam the word(s) you have entered:"))
input("Place your mouse cursor on the typing area and tap enter:")
bar = Controller().position
print("Position of mouse cursor has been logged.")
print("MAKE SURE YOU DON'T MOVE THE MOUSE!")
input("Press enter to start spamming:")
with open('words.txt', 'w') as f:
    f.write(input1)
file = open("words.txt", "r")
lines = file.readlines()
for i in range(spamvalue):
    for line in lines:
        word = str(line.rstrip())
        mouse.position = bar
        mouse.click(Button.left)
        keyboard1.type(word)
        keyboard1.press(Key.enter)
        sleep(spamtime)
print("Spamming completed!")
wait = input("Press enter to close the script:")

