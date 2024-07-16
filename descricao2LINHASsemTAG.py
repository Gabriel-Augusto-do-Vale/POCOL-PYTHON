import pyautogui
import time

# Inicia o processo
pyautogui.hotkey('alt', 'tab')
time.sleep(0.1)  # Dê tempo para a janela alternativa (se houver) aparecer

# Definindo a quantidade de repetições desejadas

    
import pyautogui
import time

# Definir o número de repetições desejado
num_repeticoes = 7

# Loop principal para repetir o código
for _ in range(num_repeticoes):
    pyautogui.moveTo(500, 375, duration=0.2)
    pyautogui.scroll(400)
    time.sleep(0.5)
    pyautogui.click()
    time.sleep(1.3)
    pyautogui.moveTo(500, 550, duration=0.2)
    pyautogui.click()
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.moveTo(500, 465, duration=0.2)
    pyautogui.click()
    pyautogui.moveTo(500, 340, duration=0.2)
    pyautogui.click()
    pyautogui.moveTo(1100, 235, duration=0.2)
    time.sleep(0.2)
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(300, 150, duration=0.2)
    pyautogui.click()
    time.sleep(0.1)

    # Rolar para cima e repetir as ações inversas
    for _ in range(17):
        pyautogui.moveTo(500, 375, duration=0.2)
        pyautogui.scroll(-108)
        time.sleep(0.1)
        pyautogui.click()
        time.sleep(1.3)
        pyautogui.moveTo(500, 550, duration=0.2)
        pyautogui.click()
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.moveTo(500, 465, duration=0.2)
        pyautogui.click()
        pyautogui.moveTo(500, 340, duration=0.2)
        pyautogui.click()
        pyautogui.moveTo(1100, 235, duration=0.2)
        time.sleep(0.2)
        pyautogui.click()
        time.sleep(1)
        pyautogui.moveTo(300, 150, duration=0.2)
        pyautogui.click()
        time.sleep(0.1)

    # Ações finais após o segundo ciclo de rolagem
    time.sleep(1)
    pyautogui.scroll(-500)
    time.sleep(1)

    pyautogui.moveTo(500, 430, duration=0.2)
    pyautogui.click()
    time.sleep(1.3)
    pyautogui.moveTo(500, 550, duration=0.2)
    pyautogui.click()
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.moveTo(500, 465, duration=0.2)
    pyautogui.click()
    pyautogui.moveTo(500, 340, duration=0.2)
    pyautogui.click()
    pyautogui.moveTo(1100, 235, duration=0.2)
    time.sleep(0.2)
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(300, 150, duration=0.2)
    pyautogui.click()
    time.sleep(0.1)

    time.sleep(0.3)
    pyautogui.moveTo(500, 500, duration=0.2)
    pyautogui.click()
    time.sleep(1.3)
    pyautogui.moveTo(500, 550, duration=0.2)
    pyautogui.click()
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.moveTo(500, 465, duration=0.2)
    pyautogui.click()
    pyautogui.moveTo(500, 340, duration=0.2)
    pyautogui.click()
    pyautogui.moveTo(1100, 235, duration=0.2)
    time.sleep(0.2)
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(300, 150, duration=0.2)
    pyautogui.click()
    time.sleep(0.5)

    # Ação final antes do próximo ciclo
    pyautogui.moveTo(1085, 590, duration=0.2)
    pyautogui.click()
    time.sleep(2)  # Tempo adicional para estabilizar antes do próximo ciclo

# Fim do processo
