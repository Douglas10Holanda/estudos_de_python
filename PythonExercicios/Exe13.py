# Exercicio 13 de Python - Reajuste Salarial

# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input("Digite o seu salário: R$ "))
aumento = salario * 15/ 100
result = salario + aumento

print('O seu salário atual é de R$ {:.2f} reais. Simulando 15% de aumento, você ganhará R$ {:.2f} reais a mais, totalizando um novo salário de R$ {:.2f} reais.'.format(salario,aumento,result))