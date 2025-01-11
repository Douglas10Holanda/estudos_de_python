# Manipulando Texto

"""
frase = 'Curso em Video Python'

[C][u][r][s][o][ ][e][m][ ][V][i][d][e][o][ ][P][y][t][h][o][n]
 0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20         = 21 caracteres


# Fatiamento de Strings

frase[9] = V
frase[9:13] = Vide
frase[9:14] = Video 
frase[9:21] = Video Python
frase[9:21:2] = VdoPto
frase[:5] = Curso
frase[15:] = Python
frase[9::3] = VePh


# Análise de Strings

- Conta o tamanho de caracteres da String
len(frase) = 21

- Conta quantas carateceres 'o' tem na string
frase.count('o') = 3

- Conta com fatiamento de string
frase.count('o', 0, 13) = 1

- Conta quantas vezes encontrou 'deo' na string
frase.find('deo') = 11

- Quando a string não existe retorna -1
frase.find('Android') = -1

- Retorna se existe 'Curso' na string
'Curso' in frase = True


# Tranformação de Strings

- Troca a string por outra
frase.replace('Python', 'Android') = Curso em Vídeo Android

- Todos os caracteres maiusculos
frase.upper() = CURSO EM VIDEO PYTHON

- Todos os caracteres minusculos
frase.lower() = curso em video python

- Primeiro caractere maiusculo e o resto minusculo
frase.capitalize() = Curso em video python

- Aplica o capitalize palavra por palavra
frase.title() = Curso Em Video Python


[ ][ ][ ][A][p][r][e][d][d][a][ ][P][y][t][h][o][n][ ][ ]
 0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18               = 19 caracteres

- Remove os caracteres inutéis
frase.strip() = [A][p][r][e][d][d][a][ ][P][y][t][h][o][n]              = 14 caracteres

- Remove os caracteres inutéis da direita
frase.rstrip() = [ ][ ][ ][A][p][r][e][d][d][a][ ][P][y][t][h][o][n]    = 17 caracteres

- Remove os caracteres inutéis da esquerda
frase.lstrip() = [A][p][r][e][d][d][a][ ][P][y][t][h][o][n][ ][ ]       = 16 caracteres


# Divisão de Strings

[C][u][r][s][o][ ][e][m][ ][V][i][d][e][o][ ][P][y][t][h][o][n]
 0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20         = 21 caracteres


- Dividi uma string em uma lista de palavras
frase.split() =  [C][u][r][s][o]   [e][m]   [V][i][d][e][o]   [P][y][t][h][o][n]
                  0  1  2  3  4     0  1     0  1  2  3  4     0  1  2  3  4  5
                [       1        ][  2   ][        3       ][         4          ]


- Juntasr uma lista de palavras com uma string
'-'.join(frase) = [C][u][r][s][o][-][e][m][-][V][i][d][e][o][-][P][y][t][h][o][n]

"""

frase = 'Curso em Video Python'
print(frase)

# Fateamento
print('\n\nFateamento de Strings \n\n')

print(frase[9])
print(frase[9:13])
print(frase[9:14])
print(frase[9:21])
print(frase[9:21:2])
print(frase[:5])
print(frase[15:])
print(frase[9::3])


# Análise
print('\n\nAnálise de Strings \n\n')

print(len(frase))
print(frase.count('o'))
print(frase.count('o', 0, 13))
print(frase.find('deo'))
print(frase.find('Android'))
print('Curso' in frase)

# Tranformação
print('\n\nTranformação de Strings \n\n')

print(frase.replace('Python', 'Android'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
print(frase.strip())
print(frase.rstrip())
print(frase.lstrip())


# Divisão de Strings
print('\n\nDivisão de Strings \n\n')

print(frase.split())
print('-'.join(frase))




