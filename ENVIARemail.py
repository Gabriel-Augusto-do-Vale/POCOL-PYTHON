import pyautogui
import time

pyautogui.hotkey('alt', 'tab')
time.sleep(0.1)

pyautogui.moveTo(860,690, duration=0.2)
for _ in range(5):
    pyautogui.click()

pyautogui.moveTo(1290,690, duration=0.2)
pyautogui.click()

time.sleep(0.5)
for _ in range(4):
    pyautogui.moveTo(725,270, duration=0.2)
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(725,400, duration=0.2)
    pyautogui.click()
    for _ in range(3):
        pyautogui.press('pagedown')
    pyautogui.press('enter')
    pyautogui.press('enter')
    pyautogui.typewrite('TEXTO 1')
    pyautogui.press('enter')
    pyautogui.press('enter')
    pyautogui.typewrite('TEXTO 1')
    pyautogui.press('enter')
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.moveTo(65, 200, duration=0.2)
    pyautogui.click()
    time.sleep(1.5)
    pyautogui.moveTo(725,270, duration=0.2)
    pyautogui.scroll(-40)