import pyautogui
import time


#UTILIZAR ESSE PROCESSO COM A PÁGINA DO GOOGLE ESTICADA NO LIMITE DE BARRA DE ROLAGEM DAS LATERAIS
# inicio do processo
pyautogui.hotkey('alt', 'tab')
pyautogui.moveTo(475, 385, duration=0.2)
pyautogui.scroll(60000)
time.sleep(1)

for _ in range(19):
    pyautogui.scroll(-515)
    time.sleep(0.2)

#time.sleep(1.5)
#pyautogui.scroll(-2000)

#time.sleep(1)
#pyautogui.moveTo(1050, 600, duration=0.2)
