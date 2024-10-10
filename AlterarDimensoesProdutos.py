import pyautogui
import time
import keyboard
import sys

class Automacao:
    def __init__(self):  
        time.sleep(0.1)
        pyautogui.click()
        time.sleep(0.1)
        time.sleep(4)

        pyautogui.moveTo(1225, 275, duration=0.2)
        time.sleep(0.1)
        pyautogui.scroll(5000)
        pyautogui.scroll(-2750)
        pyautogui.moveTo(612, 280, duration=0.2)
        pyautogui.click()
        pyautogui.press('tab')  
        pyautogui.typewrite("2000")
        pyautogui.press('tab')  
        pyautogui.press('tab')  
        pyautogui.typewrite("20")
        pyautogui.press('tab') 
        pyautogui.typewrite("30")
        pyautogui.press('tab') 
        pyautogui.typewrite("30")
        time.sleep(0.3)
        pyautogui.moveTo(1225, 275, duration=0.2)
        pyautogui.scroll(-5000)
        time.sleep(0.1)
        pyautogui.moveTo(1100, 600, duration=0.2)
        time.sleep(0.1)
        pyautogui.click()

        time.sleep(2.5)
        pyautogui.moveTo(290, 150, duration=0.2)
        pyautogui.click()
        time.sleep(2)
        pyautogui.moveTo(500, 490, duration=0.2)
        pyautogui.scroll(-90000)
        pyautogui.scroll(i*n_produto)
        time.sleep(0.3)
        

j = 1
for _ in range(5):
    pyautogui.moveTo(1225, 275, duration=0.2)
    pyautogui.scroll(-90000)
    i = 171

    if j==1:
        n_produto = 1
        for _ in range(17):
            if n_produto == 21:
                pyautogui.scroll(5000)
                pyautogui.moveTo(500, 400, duration=0.2)
                automacao = Automacao()
 
            else:
                pyautogui.moveTo(500, 460, duration=0.2)
                automacao = Automacao()

            n_produto += 1
        time.sleep(0.5)
        pyautogui.moveTo(1225, 275, duration=0.2)
        pyautogui.scroll(-90000)
        time.sleep(0.3)
        pyautogui.moveTo(1300, 595, duration=0.2)
        pyautogui.click()
        time.sleep(4)
    

    elif j==3:
        n_produto = 1
        for _ in range(19):
            if n_produto == 21:
                pyautogui.scroll(5000)
                pyautogui.moveTo(500, 400, duration=0.2)
                automacao = Automacao()

            else:
                pyautogui.moveTo(500, 460, duration=0.2)
                automacao = Automacao()

            n_produto += 1


    else:
        n_produto = 1
        for _ in range(20):
            if n_produto == 21:
                pyautogui.scroll(5000)
                pyautogui.moveTo(500, 470, duration=0.2)
                automacao = Automacao()

            else:
                pyautogui.moveTo(500, 460, duration=0.2)
                automacao = Automacao()

            n_produto += 1

        time.sleep(0.5)
        pyautogui.moveTo(1225, 275, duration=0.2)
        pyautogui.scroll(-90000)
        time.sleep(0.3)
        pyautogui.moveTo(1300, 595, duration=0.2)
        pyautogui.click()
        time.sleep(4)
    
    j += 1


