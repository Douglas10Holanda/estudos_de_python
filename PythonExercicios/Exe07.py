# Exercicio 7 de Python - Média Aritmética

# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média.

aluno = str(input('Digite o seu nome: '))

n1 = float(input("Digite a sua primeira nota: "))
n2 = float(input("Digite a sua segunda nota: "))
media = (n1+n2)/2

print('Olá {}, tudo bem? \nA sua primeira nota foi {} e sua segunda nota foi {}. \nEntão, a sua média foi: {}'.format(aluno,n1,n2,media))
