# Exercicio 6 de Python - Dobro, Triplo, Raiz Quadrada

# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = int(input("Digite um número: "))
dobro = n*2
triplo = n*3
raiz = n**(1/2)

print('O dobro de {} é igual a {}.'.format(n,dobro))
print('O triplo de {} é igual a {}.'.format(n,triplo))
print('A raiz quadrada de {} é igual a {}.'.format(n,raiz))