# Exercicio 34 de Python - Aumentos múltiplos

"""
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para
salários superiores a R$ 1250,00, calcule um aumento de 10%. Para inferiores ou iguais, o aumento é de 15%.
"""

salario = float(input('Digite o seu salário: R$ '))
aumento = 0

if salario <= 1250:
    aumento = salario + ((salario * 15)/100)
    print('O seu salário é R$ {:.2f}, com o aumento de 15% seu salário agora é R$ {:.2f}.'.format(salario, aumento))
else:
    aumento = salario + ((salario * 10)/100)
    print('O seu salário é R$ {:.2f}, com o aumento de 10% seu salário agora é R$ {:.2f}.'.format(salario, aumento))