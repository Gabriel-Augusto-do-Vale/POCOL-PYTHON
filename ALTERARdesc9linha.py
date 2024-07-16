import pyautogui
import time


#UTILIZAR ESSE PROCESSO COM A PÁGINA DO GOOGLE ESTICADA NO LIMITE DE BARRA DE ROLAGEM DAS LATERAIS
# inicio do processo
pyautogui.hotkey('alt', 'tab')

for _ in range(16):
    pyautogui.moveTo(475, 385, duration=0.2)
    pyautogui.scroll(60000)
    time.sleep(1)

    pyautogui.moveTo(475, 385, duration=0.2)
    time.sleep(0.5)
    pyautogui.scroll(4000)
    time.sleep(0.5)
    pyautogui.click()
    time.sleep(2.5)
    pyautogui.scroll(4000)
    time.sleep(0.1)
    #PROCESSO INICIADO
    #SELECIONA A DESCRICAO
    pyautogui.moveTo(475, 635, duration=0.2)
    pyautogui.click()
    time.sleep(0.2)
    pyautogui.hotkey('ctrl', 'a')
    #TERMINA A SELECAO DE DESCRICAO
    #INICIA TROCA DE FONTE
    pyautogui.moveTo(475, 480, duration=0.2)
    time.sleep(0.1)
    pyautogui.click()
    pyautogui.moveTo(475, 340, duration=0.2)
    time.sleep(0.1)
    pyautogui.click()
    #TERMINA A TROCA DE FONTE
    #INICIA TROCA DE PRODUTO E SALVA ALETRACOES
    pyautogui.moveTo(1100, 225, duration=0.2)
    pyautogui.click()
    time.sleep(2)
    pyautogui.moveTo(300, 150, duration=0.2)
    time.sleep(1)
    pyautogui.click()
    time.sleep(0.1)



    for _ in range(19):
        pyautogui.moveTo(475, 385, duration=0.2)
        pyautogui.scroll(-466)
        time.sleep(0.5)
        pyautogui.click()
        time.sleep(2)
        pyautogui.moveTo(475, 635, duration=0.2)
        pyautogui.click()
        time.sleep(0.2)
        pyautogui.hotkey('ctrl', 'a')
        #TERMINA A SELECAO DE DESCRICAO
        #INICIA TROCA DE FONTE
        pyautogui.moveTo(475, 480, duration=0.2)
        time.sleep(0.1)
        pyautogui.click()
        pyautogui.moveTo(475, 340, duration=0.2)
        time.sleep(0.1)
        pyautogui.click()
        #TERMINA A TROCA DE FONTE
        #INICIA TROCA DE PRODUTO E SALVA ALETRACOES
        pyautogui.moveTo(1100, 225, duration=0.2)
        pyautogui.click()
        time.sleep(2)
        pyautogui.moveTo(300, 150, duration=0.2)
        time.sleep(1)
        pyautogui.click()
        time.sleep(0.1)
        time.sleep(0.1)


    time.sleep(1.5)
    pyautogui.scroll(-2000)

    time.sleep(2)
    pyautogui.moveTo(1050, 600, duration=0.2)
    pyautogui.click()
    time.sleep(2)