import pyautogui
import time

pyautogui.hotkey('alt', 'tab')
time.sleep(0.1)

pyautogui.moveTo(475, 600, duration=0.2)