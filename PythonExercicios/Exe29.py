# Exercicio 29 de Python - Radar eletrônico

"""
Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem
dizendo que ele foi multado. A multa vai custar R$ 7,00 por cada Km acima do limite.
"""

vel = float(input('Qual foi sua velocidade? '))
multa = 0

if vel > 80:
    multa = 7*(vel-80)
    print('Você foi multado!')
    print('A multa vai lhe custar R$ {:.2f}'.format(multa))
else:
    print('Sem multas!')