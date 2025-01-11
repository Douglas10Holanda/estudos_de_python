# Exercicio 20 de Python - Sorteando uma ordem na lista

"""
Um professor quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que 
leia o nome dos alunos e mostre a ordem sorteada.
"""

"""import random
a1 = str(input("Digite o nome do aluno 1: "))
a2 = str(input("Digite o nome do aluno 2: "))
a3 = str(input("Digite o nome do aluno 3: "))
a4 = str(input("Digite o nome do aluno 4: "))
lista = [a1, a2, a3, a4]
random.shuffle(lista)

print("A ordem de apresentação será: ")
print(lista)"""

from random import shuffle
a1 = str(input("Digite o nome do aluno 1: "))
a2 = str(input("Digite o nome do aluno 2: "))
a3 = str(input("Digite o nome do aluno 3: "))
a4 = str(input("Digite o nome do aluno 4: "))
lista = [a1, a2, a3, a4]
shuffle(lista)

print("A ordem de apresentação será: ")
print(lista)