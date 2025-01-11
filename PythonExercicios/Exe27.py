# Exercicio 27 de Python - Primeiro e último nome de uma pessoa

"""
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
- Ex: Ana Maria de Souza
- Primeiro = Ana
- Último = Souza

"""

nome = str(input("Digite o seu nome completo: ")).strip().split()

print("O seu primeiro nome é {}.".format(nome[0]))
print("O seu segundo nome é {}.".format(nome[len(nome)-1]))