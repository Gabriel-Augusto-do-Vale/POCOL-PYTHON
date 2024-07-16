import pyautogui
import time

# inicio do processo
pyautogui.hotkey('alt', 'tab')

for _ in range(30):
    pyautogui.moveTo(600, 390, duration=0.2)
    pyautogui.scroll(400)
    pyautogui.moveTo(605, 390, duration=0.1)
    pyautogui.moveTo(595, 390, duration=0.1)
    pyautogui.click()
    time.sleep(0.1)
    pyautogui.press('backspace')
    for _ in range(18):
        pyautogui.scroll(-205)
        pyautogui.moveTo(605, 390, duration=0.1)
        pyautogui.click()
        time.sleep(0.1)
        pyautogui.press('backspace')
        pyautogui.moveTo(595, 390, duration=0.1)

    pyautogui.scroll(-1000)
    pyautogui.moveTo(600, 430, duration=0.2)
    pyautogui.click()
    time.sleep(0.1)
    pyautogui.press('backspace')

    time.sleep(0.1)
    pyautogui.moveTo(1075, 600, duration=0.2)
    pyautogui.click()
    time.sleep(2)

