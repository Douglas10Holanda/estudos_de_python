# Exercicio 18 de Python - Seno, Cosseno e Tangente

# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

"""
import math
ang = int(input("Digite o angulo: "))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))

print("O ângulo de {} tem o SENO de {:.2f}".format(ang,sen))
print("O ângulo de {} tem o COSSENO de {:.2f}".format(ang,cos))
print("O ângulo de {} tem a TANGENTE de {:.2f}".format(ang,tan))
"""


from math import sin,cos,tan,radians
ang = int(input("Digite o angulo: "))
sen = sin(radians(ang))
coss = cos(radians(ang))
tang = tan(radians(ang))

print("O ângulo de {} tem o SENO de {:.2f}".format(ang,sen))
print("O ângulo de {} tem o COSSENO de {:.2f}".format(ang,coss))
print("O ângulo de {} tem a TANGENTE de {:.2f}".format(ang,tang))