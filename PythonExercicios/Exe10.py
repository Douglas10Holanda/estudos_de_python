# Exercicio 10 de Python - Conversor de Moedas

# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Doláres ela pode comprar.
# Considere US$ 1,00 = R$ 3,27

real = float(input("Quanto dinheiro você tem na sua carteira? \nR$ "))
dolar = real // 3.27

print('Você pode comprar exatamente {:.0f} dólares.'.format(dolar))