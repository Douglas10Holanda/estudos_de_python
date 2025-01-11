# Exercicio 4 de Python - Dissecando uma váriável

# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

coisa = input("Digite algo: ")

print('O tipo primitivo desse valor é ', type(coisa))
print('Só tem espaços? ', coisa.isspace())
print('É um número? ', coisa.isnumeric())
print('É alfabético? ', coisa.isalpha())
print('É alfanúmerico? ', coisa.isalnum())
print('É maiuscula? ', coisa.isupper())
print('É minusculo? ', coisa.islower())
print('Está capitalizada? ', coisa.istitle())
