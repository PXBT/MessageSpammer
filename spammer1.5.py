from time import sleep
import sys
import subprocess
print("Made by PXBT_OCT, 2021")
sleep(0.2)
print("Thanks to SpookySec for original code.")
print("Version 1.5, Build Date: 17 Oct 2021")
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

