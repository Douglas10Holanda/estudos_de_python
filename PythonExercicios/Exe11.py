# Exercicio 11 de Python - Pintando Parede

""" Faça um programa que leia a largura e altura de uma parede em metros, calcule sua área e a quantidade de tinta necessária para
pinta-la, sabendo que cada litro de tinta, pinta uma área de 2m². """

altura = float(input("Digite a altura da parede: "))
largura = float(input("Digite a largura da parede: "))
area = altura * largura
tinta = area / 2


print('A largura da parede é: {}'.format(largura))
print('A altura da parede é: {}'.format(altura))
print('A parede tem uma dimensão de {}x{} e sua área é de {}m².'.format(largura,altura,area))
print('Para conseguir pintar esta parede, você vai precisar de {}l de tinta.'.format(tinta))