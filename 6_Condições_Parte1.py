# Condições Simples e Compostas

"""
if carro.esquerda():
    bloco True
else:
    bloco False


if = Estrutura Simples
if, else = Estrutua Composta

Exemplo:

tempo = int(input('Quantos anos tem seu carro?'))
if tempo <= 3:
    print('Carro novo')
else:
    print('Carro velho')
print('---FIM---')


# Condição Simplificada

tempo = int(input('Quantos anos tem seu carro?'))
print('Carro novo' if tempo <= 3 else 'Carro velho')
print('---FIM---')

"""

nome = str(input('Qual o seu nome? '))

if nome == 'Douglas':
    print('Que nome Lindo você tem!')
else:
    print('Que nome esquisito você tem!')
print('Bom dia, {}!'.format(nome))


n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
media = (n1+n2)/2
print("A sua média foi {:.1f}".format(media))

if media >= 7:
    print("Parabéns, você foi aprovado!")
else:
    print("Você foi reprovado, estude mais!")


k1 = float(input('Digite sua primeira nota: '))
k2 = float(input('Digite sua segunda nota: '))
m = (k1+k2)/2
print("A sua média foi {:.1f}".format(m))

if m >= 7:
    print("APROVADO!")
elif m >= 5 and m < 7:
    print("Você ficou de recuperação, estude para a avaliação final!")
else:
    print("REPROVADO!")