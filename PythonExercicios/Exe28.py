# Exercicio 28 de Python - Jogo da Adivinhação v.1.0

"""
Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar
descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
"""

import random
from time import sleep

n = random.randint(1,5)                                             # Faz o computador pensar em um número
num = int(input("Qual número de 0 a 5 o computador pensou? "))      # Jogador tenta adivinhar

print("PROCESSANDO...")
sleep(2)
if num == n:                                                        # Verifica se o jogador acertou ou errou
    print("Paravéns, você \nO número pensado foi: {}".format(n))
else:
    print("Que pena, você errou! \nO número pensado foi: {}".format(n))