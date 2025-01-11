# Exercicio 12 de Python - Calculando Descontos

# Faça um algoritmo que leia um preço de um produto e mostre o seu novo preço, com 5% de desconto.

produto = str(input("Digite o nome do produto: "))
preco = float(input("Digite o valor do produto: R$ "))
desc = preco * 5 / 100
result = preco - desc


print('Você comprou um {} no valor de R$ {} reais. Com o desconto aplicado o novo valor do produto é de R$ {:.2f} reais.\n Você economizou R$ {:.2f} reais. '.format(produto,preco,result,desc))