# Exercicio 32 de Python - Ano Bissexto

# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

from datetime import date

ano =  int(input('Digite o ano que quer analisar ou digite 0 para analisar o ano atual: '))

if ano == 0:
    ano = date.today().year
    
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO!'.format(ano))
else:
    print('O ano {} é NÃO É BISSEXTO!'.format(ano))