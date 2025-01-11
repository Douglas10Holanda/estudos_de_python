# Exercicio 16 de Python - Quebrando um número

# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.
"""
Ex: Digite um número: 6.127
O número 6.127 tem a parte inteira 6.
"""

import math 
num = float(input("Digite um número: "))
# truncando a parte inteira
print("O número {} tem a parte inteira {}".format(num, math.trunc(num)))
# arredondando o valor para baixo
print("{} = {}".format(num, math.floor(num)))
# sem usar módulo
print("{} = {}".format(num, int(num)))