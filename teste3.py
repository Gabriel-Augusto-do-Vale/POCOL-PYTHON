import pyautogui
import time

# inicio do processo
pyautogui.hotkey('alt', 'tab')
time.sleep(0.1)

for _ in range(3): #LOOP QUANTIDADE DE PÁGINAS A SEREM FEITAS
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
    pyautogui.moveTo(1100, 230, duration=0.2)
    pyautogui.click()
    time.sleep(2)
    pyautogui.moveTo(300, 150, duration=0.2)
    time.sleep(1)
    pyautogui.click()
    #FIM DO PRIMEIRO PRODUTO DA PAGINA

    #FAZ TODOS OS 18 PRODUTOS DO MEIO
    for _ in range(18):
        #SELECIONA O NOVO PRODUTO
        pyautogui.moveTo(475, 385, duration=0.2)
        pyautogui.scroll(-230)
        time.sleep(0.3)
        pyautogui.click()
        #PROCESSO INICIADO
        #SELECIONA A DESCRICAO
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
        pyautogui.moveTo(1100, 230, duration=0.2)
        pyautogui.click()
        time.sleep(2)
        pyautogui.moveTo(300, 150, duration=0.2)
        time.sleep(1)
        pyautogui.click()
        #FIM DO PRIMEIRO PRODUTO DA PAGINA

    #FAZ O ÚLTIMO PRODUTO
    time.sleep(0.5)
    pyautogui.moveTo(475, 455, duration=0.2)
    pyautogui.scroll(-2000)
    time.sleep(1)
    pyautogui.moveTo(475, 435, duration=0.2)
    pyautogui.click()
    time.sleep(2.5)
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
    pyautogui.moveTo(1100, 230, duration=0.2)
    pyautogui.click()
    time.sleep(2)
    pyautogui.moveTo(300, 150, duration=0.2)
    time.sleep(1)
    pyautogui.click()
    #FIM DO PRIMEIRO PRODUTO DA PAGINA

    #TROCA DE PÁGINA
    time.sleep(0.5)
    pyautogui.moveTo(1075, 600, duration=0.2)
    pyautogui.click()
    time.sleep(2.5)






        