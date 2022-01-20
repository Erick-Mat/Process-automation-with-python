# Automação de Sistemas e Processos com Python

import pyautogui
import pyperclip
import time
import pandas as pd

pyautogui.PAUSE = 1.5 # tempo

# Passo 1: entrar no sistema da empresa(link do drive)
pyautogui.hotkey('ctrl','t')
pyperclip.copy('https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga?usp=sharing')
pyautogui.hotkey('ctrl','v')
pyautogui.press('enter')

time.sleep(5)

# Passo 2: navegar no sistema (até a pasta Exportar)
pyautogui.click(x=383, y=296, clicks=2)
time.sleep(2)

# Passo 3: fazer download da base de vendas
pyautogui.click(x=447, y=448)
pyautogui.click(x=1473, y=189)
pyautogui.click(x=1261, y=624)
time.sleep(4)

# Passo 4: importar a base de vendas pro python

tabela = pd.read_excel(r'C:\Users\erick\Downloads\Vendas - Dez.xlsx')
print(tabela)

# Passo 5: calcular o faturamento e quantidade de produtos vendidos
faturamento = tabela['Valor Final'].sum()
qtde_produtos = tabela['Quantidade'].sum()


# Passo 6: abrir e-mail
pyautogui.hotkey('ctrl','t')
pyperclip.copy('https://mail.google.com/mail/u/0/#inbox')
pyautogui.hotkey('ctrl','v')
pyautogui.press('enter')
time.sleep(6)

# escrever o e-mail
pyautogui.click(x=84, y=197)
pyautogui.write('erick.mattar3@gmail.com')
pyautogui.press('tab')
pyautogui.press('tab')
pyperclip.copy('Relatório de Vendas.')
pyautogui.hotkey('ctrl','v')
pyautogui.press('tab')

texto = f'''
Prezados, bom dia

O faturamento de ontem foi de R${faturamento:,.2f}
A quantidade de produtos foi de: {qtde_produtos:,}

Abs
Erick
'''

pyperclip.copy(texto)
pyautogui.hotkey('ctrl','v')
pyautogui.hotkey('ctrl','enter')
