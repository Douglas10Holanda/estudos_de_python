# Exercicio 25 de Python - Procurando uma string dentro de outra

"""
Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

"""

nome = str(input("Digite seu nome completo: ")).strip()
print( "Seu nome tem Silva?\n {}".format('SILVA' in nome.upper()))