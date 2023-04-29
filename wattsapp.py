import pyautogui
import time
time.sleep(3)
count=0
while count<=5:
    pyautogui.typewrite("pappu"+str(count))
    pyautogui.press("enter")
    count=count+1
