# Exercicio 5 de Python - Antecessor e Sucessor

# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e antecessor

num = int(input("Digite um número: "))
# sucessor
suc = num+1
# antecessor
ant = num-1

print("O número escolhido foi {}. O seu sucessor é o número {} e seu antecessor é o número {}.".format(num,suc,ant))


# ----- OUTRA FORMA DE RESOLVER -----

n = int(input("Digite um número: "))
print("Analisando o número {}, o seu sucessor é {} e seu antecessor é {}.".format(n, (n+1),(n-1)))