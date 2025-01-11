# Operadores Aritméticos

# "+"  Adição
# "-"  Subtração
# "*"  Multiplicação
# "/"  Divisão
# "**" Potência
# "//" Divisão Inteira
# "%"  Resto da Divisão (módulo)


# 5+2 == 7
# 5-2 == 3
# 5*2 == 10
# 5/2 == 2.5
# 5**2 == 25
# 5//2 == 2
# 5%2 == 1


# ----- ORDEM DE PRECEDÊNCIA -----
# 1 - "()"
# 2 - "**"
# 3 - "*" "/" "//" "%"
# 4 - "+" "-"

# Exemplos

n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))

som = n1 + n2
sub = n1 - n2
mult = n1 * n2
div = n1 / n2 
pot = n1 ** n2
divint = n1 // n2
mod = n1 % n2

print('A soma entre {} e {} é igual a {}'.format(n1,n2,som))
print('A subtração entre {} e {} é igual a {}'.format(n1,n2,sub))
print('A multiplicação entre {} e {} é igual a {}'.format(n1,n2,mult))
print('A divisão entre {} e {} é igual a {}'.format(n1,n2,div))
print('A potencia entre {} e {} é igual a {}'.format(n1,n2,pot))
print('A divisão inteira entre {} e {} é igual a {}'.format(n1,n2,divint))
print('O resto da divisão entre {} e {} é igual a {}'.format(n1,n2,mod))