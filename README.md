# Process-automation-with-python
Automatização de processos manuais e repetitivos utilizando python.

## Sobre:

Todos os dias, o sistema atualiza as vendas do dia anterior. Este programa tem como intuito substituir o trabalho diário como analista.
Nele é enviado um e-mail para a diretoria com o faturamento e a quantidade de produtos vendidos no dia anterior, usando como base as seguintes bibliotecas:

- pyautogui: PyAutoGUI permite que seus scripts Python controlem o mouse e o teclado para automatizar as interações com outros aplicativos. 
- pyperclip: O Pyperclip fornece um módulo Python multiplataforma para copiar e colar texto na área de transferência.
- time: Permite a utilização de várias funções relacionadas à tempo.
- pandas: é uma biblioteca de software criada para a linguagem Python para manipulação e análise de dados.

## Limitações: 

- PyAutoGUI: O PyAutoGUI funciona no Windows, macOS e Linux e é executado no Python 2 e 3. O PyAutoGUI não funciona em segundo plano.
- Pyperclip: O PyAutoGUI não consegue escrever ou interpretar caracteres especiais. Para ultrapassar esse problema utilizamos a biblioteca Pyperclip.
- Time: O PyAutoGUI possui um temporizador que pode ser utilizado, funcionando somente se estiver entre comandos da propria biblioteca. Para um temporizador geral é necessário utilizar a biblioteca Time.

## Instalação e Execução: 

### Instalação:
- PyAutoGUI: pip install pyautogui
- Pyperclip: pip install pyperclip
- Pandas: pip install pandas

### Execução:
- python AutomatizacaoDeProcessos.py
