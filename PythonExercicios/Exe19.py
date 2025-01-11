# Exercicio 19 de Python - Sorteando um item na lista

"""
Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o 
nome deles e escrevendo  nome do aluno escolhido.
"""

"""import random
a1 = str(input("Digite o nome do aluno 1: "))
a2 = str(input("Digite o nome do aluno 2: "))
a3 = str(input("Digite o nome do aluno 3: "))
a4 = str(input("Digite o nome do aluno 4: "))
lista = [a1, a2, a3, a4]
sorteio = random.choice(lista)

print("O aluno escolhido foi: {}".format(sorteio))"""

from random import choice
a1 = str(input("Digite o nome do aluno 1: "))
a2 = str(input("Digite o nome do aluno 2: "))
a3 = str(input("Digite o nome do aluno 3: "))
a4 = str(input("Digite o nome do aluno 4: "))
lista = [a1, a2, a3, a4]
sorteio = choice(lista)

print("O aluno escolhido foi: {}".format(sorteio))