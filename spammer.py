import pip
print("Installing required libraries (pynput)...")
pip.main(["install", "pynput"])
print("Pynput has been installed!")
from pynput.mouse import Controller, Button
from pynput import keyboard
from pynput.keyboard import Key
from time import sleep
keyboard1 = keyboard.Controller()
mouse = Controller()
input1 = input("Enter what word(s) should be spammed and tap enter:")
spamvalue = int(input("Enter number of times to spam the word(s) you have entered:"))
input("Place your mouse cursor on the typing area and tap enter:")
bar = Controller().position
print("Position of mouse cursor has been logged.")
print("MAKE SURE YOU DON'T MOVE THE MOUSE!")
input("Press enter to continue:")
print("The script will automatically close once completed.")
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

