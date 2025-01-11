# Exercicio 31 de Python - Custo da Viagem

"""
Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem,
cobrando R$0,50 por km para viagens de até 200km e R$0,45 para viagens mais longas. 
"""

dist = int(input('Digite a distância da viagem: '))

if dist <= 200:
    preco = dist * 0.50
    print('A distancia é de {} km e o preço da passagem é de R${:.2f}.'.format(dist,preco))
else:
    preco = dist * 0.45
    print('A distancia é de {} km e o preço da passagem é de R${:.2f}.'.format(dist,preco))