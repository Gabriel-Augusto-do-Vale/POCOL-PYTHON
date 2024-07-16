import pyautogui
import time


#UTILIZAR ESSE PROCESSO COM A PÁGINA DO GOOGLE ESTICADA NO LIMITE DE BARRA DE ROLAGEM DAS LATERAIS
# inicio do processo
pyautogui.hotkey('alt', 'tab')

for _ in range(1):
    pyautogui.moveTo(300, 385, duration=0.2)
    pyautogui.scroll(6000)
    time.sleep(0.5)

    ###########################ENTRAR NO PRODUTO E SELECIONAR A DESCRICAO
    pyautogui.click()
    pyautogui.moveTo(475, 635, duration=0.2)
    time.sleep(2)
    pyautogui.click()
    time.sleep(0.2)
    pyautogui.hotkey('ctrl', 'a')
    #############################SELECIONAR TIPO DE FONTE DA DESCRICAO
    pyautogui.moveTo(375, 480, duration=0.2)
    time.sleep(0.1)
    pyautogui.click()
    pyautogui.moveTo(375, 330, duration=0.2)
    time.sleep(0.1)
    pyautogui.click()
    ################################SAIR DO PRODUTO
    pyautogui.moveTo(1015, 230, duration=0.2)
    pyautogui.click()
    time.sleep(2)
    pyautogui.moveTo(40, 150, duration=0.2)
    time.sleep(0.5)
    pyautogui.click()



    for _ in range(18):
        pyautogui.moveTo(300, 385, duration=0.2)
        pyautogui.scroll(-138)
        time.sleep(0.5)
        ###########################ENTRAR NO PRODUTO E SELECIONAR A DESCRICAO
        pyautogui.click()
        pyautogui.moveTo(475, 635, duration=0.2)
        time.sleep(2)
        pyautogui.click()
        time.sleep(0.2)
        pyautogui.hotkey('ctrl', 'a')
        #############################SELECIONAR TIPO DE FONTE DA DESCRICAO
        pyautogui.moveTo(375, 480, duration=0.2)
        time.sleep(0.1)
        pyautogui.click()
        pyautogui.moveTo(375, 330, duration=0.2)
        time.sleep(0.1)
        pyautogui.click()
        ################################SAIR DO PRODUTO
        pyautogui.moveTo(1015, 230, duration=0.2)
        pyautogui.click()
        time.sleep(2)
        pyautogui.moveTo(40, 150, duration=0.2)
        time.sleep(0.5)
        pyautogui.click()

    time.sleep(1.5)
    pyautogui.scroll(-200)
    pyautogui.moveTo(300, 480, duration=0.2)
    ###########################ENTRAR NO PRODUTO E SELECIONAR A DESCRICAO
    pyautogui.click()
    pyautogui.moveTo(475, 635, duration=0.2)
    time.sleep(2)
    pyautogui.click()
    time.sleep(0.2)
    pyautogui.hotkey('ctrl', 'a')
    #############################SELECIONAR TIPO DE FONTE DA DESCRICAO
    pyautogui.moveTo(375, 480, duration=0.2)
    time.sleep(0.1)
    pyautogui.click()
    pyautogui.moveTo(375, 330, duration=0.2)
    time.sleep(0.1)
    pyautogui.click()
    ################################SAIR DO PRODUTO
    pyautogui.moveTo(1015, 230, duration=0.2)
    pyautogui.click()
    time.sleep(2)
    pyautogui.moveTo(40, 150, duration=0.2)
    time.sleep(0.5)
    pyautogui.click()


    time.sleep(0.5)
    pyautogui.moveTo(1035, 590, duration=0.2)
    pyautogui.click()
    time.sleep(2)



    