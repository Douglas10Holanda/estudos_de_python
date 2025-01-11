# Exercicio 24 de Python - Verificando as primeiras letras de um texto

""" 
Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'SANTO'.

"""

# Minha Solução
city = str(input("Digite a sua cidade: "))
print("{}".format('Santo' in city.strip().capitalize()))

# Solução do vídeo
cid = str(input("Em qual cidade você nasceu?\n")).strip()
print(cid[:5].upper() == 'SANTO')