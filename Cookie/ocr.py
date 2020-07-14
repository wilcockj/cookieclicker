import cv2
import pyautogui
import time
im = pyautogui.screenshot(region=(3214,551, 3262,588))
location = pyautogui.locateOnScreen(im)
while True:
    time.sleep(2)
    print(location)
