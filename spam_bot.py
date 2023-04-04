import pyautogui as pc
import time as t

string = input("what do you want to be spammed? ")  # ask string to spam
string = str(string)
num = input("How many times do you want it to be spammed? ")
num = int(num)

t.sleep(10)  # 10 seconds time to put cursor in the right place

# taking control of keyboard
# number after range is the amount of times the string gets spammed
for x in range(num):
    pc.write(string)  # the string is what will get spammed
    pc.press('enter')