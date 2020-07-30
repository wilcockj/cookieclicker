# CookieclickerAutoPlayer
Autoclicker/Bot using PyAutoGUI to automatically play cookie clicker.
Will currently click the cookie in order to increase the amount per second,
it will also periodically check the screen to see if it detects a golden cookie which gives a bonus, and will locate it and click it if present.
Also has auto upgrade functionality and purchases buildings to maximize cookies per second.
Will have to be tuned to your specific resolution

In action here
https://www.youtube.com/watch?v=xXBgPU8wmTE

Usage run cookieclickernew.py while you have the cookie clicker website in view with no obstructions

Is currently set up to run on a setup with 1366x768 monitor to the right of a 1920x1080

To setup the different resolutions in the commandline type python or python3 depending on your setup

Then import pyautogui and then type pyautogui.displayMousePosition() to start a program that will tell you your mouse position as well as the rgb colors at that pixel.
