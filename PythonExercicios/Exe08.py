# Exercicio 8 de Python - Conversor de Medidas

# Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milímetros.

# metro
medida = float(input("Digite o valor em metros: "))
# centimetro
cm = medida*100 
# milimetro
mm = medida*1000

print("A medida em metros é {}m. Portanto, o seu valor convertido para centimetros é de {:.0f}cm e seu valor convertido para milimetros é de {:.0f}mm.".format(medida,cm,mm))