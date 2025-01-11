# Exercicio 17 de Python - Catetos e Hipotenusa

""" 
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule 
e mostre o comprimento da hipotenusa.
"""

""" Forma matemática

co = float(input("Digite o valor do cateto oposto: "))
ca = float(input("Digite o valor do cateto adjacente: "))
hip = (co ** 2 + ca ** 2) ** (1/2)

print("O cateto oposto é {} e o cateto adjacente é {}, portanto o comprimento da hipotenusa é: {:.2f}".format(co,ca,hip))
"""

# Forma utilizando módulos

from math import hypot
co = float(input("Digite o valor do cateto oposto: "))
ca = float(input("Digite o valor do cateto adjacente: "))
# função pra calcular hipotenusa
hip = hypot(co, ca)
print("O cateto oposto é {} e o cateto adjacente é {}, portanto o comprimento da hipotenusa é: {:.2f}".format(co,ca,hip))