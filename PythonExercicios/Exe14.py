# Exercicio 14 de Python - Conversor de Temperaturas

# Escreva um programa que converta uma temperatura digitada em °C e converta para °F.

c = float(input("Digite uma temperatura em graus celsius: "))
f = c * 1.8 + 32

print("A temperatura de {:.1f}°C, em fahrenheit é de {:.1f}°F.".format(c,f))