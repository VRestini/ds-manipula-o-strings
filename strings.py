import os
os.system("cls")

texto ="Hoje vamos aprender a manipular strings"

# Exibe a string inteira
print(texto)

# Exibe o primeiro elemento da string
print(texto[0])

# Exibe o último elemento da string
print(texto[-1])

# Exibe o trecho de uma string
print(texto[3:10])

# Exibe um trecho de trás pra frente
print(texto[-3:-1])

# Exbie do início até sla
print(texto[:8])

# Exibe a partir do sla
print(texto[8:])

# Captura um trecho de uma string e joga em outra
trecho = texto[5:10]
print(trecho)

# Segue de 2 em 2
print(texto[0:20:2])
print(texto[::2])

# Exibe a sptring a prtir da contagem
print(texto[::-1])

# retorna o primeiro indice onde se encontra a letra
print(texto.find('a'))
print(texto('vamos'))

'''
EXERCICIOS:

1. Dada uma palavra ( mais de um caractere) pelo usuario,
exibir quantas palavras existem no texto.

2. Coloque numa segunda string o conteudo da primeira ao contrario.

3. Contar quantas letras (fornecidas pelo usuario) existem na string.
'
'''