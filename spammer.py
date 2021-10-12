from time import sleep
sleep(0.2)
print("Made by Vidhun Nagarajan, 2021")
sleep(0.2)
print("Thanks to SpookySec for original code.")
sleep(0.2)
print("Installing required libraries (pynput)...")
try:
    import pynput
    print("Pynput library already installed! Skipping installation...")
except ImportError:
    print("Pynput library not installed! Installing...")
    from pip._internal import main as pip
    pip(['install', '--user', 'pynput'])
    print("Pynput has been installed!")
from pynput.mouse import Controller, Button
from pynput import keyboard
from pynput.keyboard import Key
keyboard1 = keyboard.Controller()
mouse = Controller()
input1 = input("Enter what word(s) should be spammed and tap enter:")
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
        sleep(0.4)
print("Script completed!")
wait = input("Press enter to close the script:")

