# Exercicio 15 de Python - Aluguel de Carros    

""" Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais
ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$0,15 por Km rodado. """

km = float(input("Digite a quantidade de Km percorridos: "))
dia = int(input("Digite a quantidade de dias alugados: "))

precokm = km * 0.15
precodia = dia * 60
total = precokm + precodia
solucao = (km*0.15)+(dia*60)

print("O valor que deve ser pago pelo carro é de R$ {:.2f} reais.".format(solucao))