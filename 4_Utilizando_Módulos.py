# Utilizando Módulos

"""
bebida [café, água, suco, refrigerante, leite] | comida [pizza, hotdog, coxinha, hamburguer, ovo] | doce [pudim, cocada, chocolate]

1 - Este comando importa todas as funcionalides do módulo (comando generalista)
"import bebida" [café, água, suco, refrigerante, leite]

2- Este comando importa apenas a funcionalidade que você escolher (comando especifico)
"from doce import pudim" [pudim]
"""

# Função Math

""" 
Math [ceil, floor, trunc, pow, sqrt, factorial]

"import math" [ceil, floor, trunc, pow, sqrt, factorial]

"from math import sqrt" [sqrt]

"from math import sqrt, ceil" [sqrt, ceil]
"""

# EXEMPLO 1

import math
num = int(input("Digite um número: "))
raiz = math.sqrt(num)
print('A raiz quadrada do número {} é igual a {:.2f}.'.format(num, raiz))
print('A raiz quadrada do número {} arredondada para cima é igual a {}.'.format(num, math.ceil(raiz)))
print('A raiz quadrada do número {} arredondada para baixo é igual a {}.'.format(num, math.floor(raiz)))

""" EXEMPLO 2

from math import sqrt, floor, ceil
num = int(input("Digite um número: "))
raiz = sqrt(num)
print('A raiz quadrada do número {} é igual a {:.2f}.'.format(num, raiz))
print('A raiz quadrada do número {} arredondada para cima é igual a {}.'.format(num, ceil(raiz)))
print('A raiz quadrada do número {} arredondada para baixo é igual a {}.'.format(num, floor(raiz)))
"""

import random
n = random.random()
n1 = random.randint(1,10)
print(" {} \n {}".format(n,n1))