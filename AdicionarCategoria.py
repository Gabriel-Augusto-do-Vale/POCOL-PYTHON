import pyautogui
import time
######################################################################################################
##############################VARIAVEIS EDITAVEIS#####################################################
quantidade_pag = 1 #quantidade de páginas que o programa vai rodar
primeira_pag = 17 #quantidade de produtos que deseja ser alterado na primeira página (de baixo para cima em ordem)
ultima_pag = 19 #quantidade de produtos que deseja ser alterado na última página (de baixo para cima em ordem)
distancia = 172 #distancia exata de um produto e outro 
altura_ultimo_produto = 480 #altura da descrição do ultimo produto da página
altura_primeiro_produto = 400 #altura da descrição do primeiro produto da página
voltar = 290 #localização (horizontal) do botão de voltar de um produto
if_n_produto = 0 #1 para acionar, 0 para não acionar a variavel "altura_primeiro_produto" 
categoria = "Correia Synchroflex"
##############################VARIAVEIS EDITAVEIS#####################################################



##############################VARIAVEIS FIXAS#########################################################
i = 1
##############################VARIAVEIS FIXAS#########################################################



##############################CRIAÇÃO DE CLASSES######################################################
class Troca:
    def __init__(self):
        time.sleep(0.5)
        pyautogui.moveTo(1225, 275, duration=0.2)
        pyautogui.scroll(-90000)
        time.sleep(0.3)
        pyautogui.moveTo(1300, 595, duration=0.2)
        pyautogui.click()
        time.sleep(4)

class Automacao:
    def __init__(self):  
        time.sleep(0.1)
        pyautogui.click()
        time.sleep(0.1)
        time.sleep(4)
        pyautogui.moveTo(1225, 275, duration=0.2)
        time.sleep(0.1)
        pyautogui.scroll(5000)
        
        pyautogui.moveTo(1225,275, duration=0.2)
        time.sleep(0.1)
        pyautogui.scroll(5000)
        pyautogui.scroll(-3150)
        pyautogui.moveTo(500,460, duration=0.2)###y = 500 para uma linha, y=540 para duas linhas
        time.sleep(0.1)
        pyautogui.click()
        pyautogui.moveTo(1225,250, duration=0.2)
        pyautogui.click()
        pyautogui.typewrite(categoria)
        time.sleep(0.2)
        pyautogui.moveTo(1250, 380, duration=0.2)
        time.sleep(0.2)
        pyautogui.click()
        time.sleep(0.1)
        pyautogui.press('esc')

        time.sleep(0.3)
        pyautogui.moveTo(1225, 275, duration=0.2)
        pyautogui.scroll(-5000)
        time.sleep(0.1)
        pyautogui.moveTo(1100, 600, duration=0.2)
        time.sleep(0.1)
        pyautogui.click()
        time.sleep(2.5)
        pyautogui.moveTo(voltar, 150, duration=0.2)
        pyautogui.click()
        time.sleep(2)
        pyautogui.moveTo(500, 490, duration=0.2)
        pyautogui.scroll(-90000)
        pyautogui.scroll(distancia*n_produto)
        time.sleep(0.3)
##############################CRIAÇÃO DE CLASSES######################################################



##############################FUNCIONAMENTO DO PROGRAMA###############################################
for _ in range(quantidade_pag):
    pyautogui.moveTo(1225, 275, duration=0.2)
    pyautogui.scroll(-90000)

    if i==1:
        n_produto = 1
        for _ in range(primeira_pag):
            if n_produto == primeira_pag and if_n_produto == 1:
                pyautogui.scroll(5000)
                pyautogui.moveTo(500, altura_primeiro_produto, duration=0.2)
                automacao = Automacao()
 
            else:
                pyautogui.moveTo(500, altura_ultimo_produto, duration=0.2)
                automacao = Automacao()

            n_produto += 1

        #troca = Troca()
    

    elif i==3:
        n_produto = 1
        for _ in range(ultima_pag):
            if n_produto == ultima_pag and if_n_produto == 1:
                pyautogui.scroll(5000)
                pyautogui.moveTo(500, altura_primeiro_produto, duration=0.2)
                automacao = Automacao()

            else:
                pyautogui.moveTo(500, altura_ultimo_produto, duration=0.2)
                automacao = Automacao()

            n_produto += 1


    else:
        n_produto = 1
        for _ in range(20):
            if n_produto == 20 and if_n_produto == 1:
                pyautogui.scroll(5000)
                pyautogui.moveTo(500, altura_primeiro_produto, duration=0.2)
                automacao = Automacao()

            else:
                pyautogui.moveTo(500, altura_ultimo_produto, duration=0.2)
                automacao = Automacao()

            n_produto += 1

        #troca = Troca()
    
    i += 1
##############################FUNCIONAMENTO DO PROGRAMA###############################################

