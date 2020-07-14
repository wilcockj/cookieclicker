import cv2
import pyautogui
import time
location = pyautogui.locateOnScreen("images/cookie.png")
while True:
    time.sleep(2)
    print(location)
