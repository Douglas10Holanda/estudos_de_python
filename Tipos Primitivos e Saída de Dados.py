# TIPOS PRIMITIVOS

# int = 7, -4, 0, 9045
# float = 4.5, 0.078, -15.832, 7.0 
# bool = true, false
# str = 'Olá', '7.5', '5', ''

n1 = input("Digite um número: ")
n2 = int(input("Digite um número: "))
n3 = int(input("Digite outro número: "))
soma = n2 + n3

print(type(n1))
print(type(n2))

# Sintaxe antiga
print('A soma de ', n2, ' com ', n3, ' é igual a ', soma)
# Sintaxe nova
print('O resultado da soma entre {} e {} é igual a {}'.format(n2,n3,soma))

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
result = num1 * num2

print('A soma entre {0} e {1} é igual a {2}'.format(num1,num2,result))

objeto = str(input("Digite o nome de um objeto: "))
print("Douglas comprou um(a) {}".format(objeto))
print(type(objeto))
print(objeto.isnumeric())
