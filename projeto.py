# Projeto para Automação de tarefas em Python
# Importando todas as bibliotecas que serão utilizadas no projeto
import pyautogui as pa
import pandas as pd 
import numpy as np #biblioteca auxiliar do pandas 
import openpyxl as op # biblioteca auxiliar do pandas 
import time

pa.PAUSE=1 # Temporizador para rodar cada linha de código  a cada meio segundo

#1.Automatizar a entrada ao navegador 
pa.press('win')
pa.write('opera GX')
pa.press('enter')

#2. Automatizar a entrada ao site
pa.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pa.press('enter')

#3. Login   
pa.click(x=831, y=387)  
pa.write('Karolainysousa40@gmail.com')
pa.press('tab') 
pa.write('karolainy28)')
pa.press('tab')
pa.press('enter')
time.sleep(3)

#4. banco de dados
df=pd.read_csv('produtos.csv')        

print(df.head(n=5))

#5. Cadastrar produtos
 
for linha in df.index:
    pa.click(727, y=280)
    pa.write(str(df.loc[linha,'codigo']))
    pa.press('tab')
    
    pa.write(str(df.loc[linha,'marca']))
    pa.press('tab')

    pa.write(str(df.loc[linha,'tipo']))
    pa.press('tab')

    pa.write(str(df.loc[linha,'categoria']))
    pa.press('tab')

    pa.write(str(df.loc[linha,'preco_unitario']))
    pa.press('tab')

    pa.write(str(df.loc[linha,'custo']))
    pa.press('tab')

    obs=(str(df.loc[linha,'obs']))
    if obs != 'nan':
       pa.write(obs)
    pa.press('tab')
    pa.press('enter')
    pa.scroll(5000)
      
    

