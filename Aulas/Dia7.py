# Adicionando comentario
# para adicionar em uma linha "#"
# para adicionar em bloco ''' '''

# Strings e Números
# String = STR (Texto) representado com aspas simples ou duplas.
# Número = INT (Inteiro) ou FLOAT (Decimal) representado sem aspas.
# Booleano = BOOL (Verdadeiro ou Falso) representado sem aspas.

# Entendendo sobre Variáveis
# Variáveis são espaços de memória que armazenam valores.
# As variáveis são declaradas com um nome e um valor.
# Exemplo: nome = 'João'
# O nome da variável é 'nome' e o valor é 'João'.
# As variáveis podem ser alteradas a qualquer momento.
# Exemplo: x = 10

'''
# Modificando tipo de dados 
Para converter um tipo de dado em outro, podemos usar funções específicas.
Exemplo: 
x = str(3)
y = int(4)
z = float(5)

print(x + x)
print(y + y)
print(z + z)'
'''
'''
# Praticando com Strings e Integers
# O Julio tem 24 anos de idade e mora em Belo Horizonte.

nome = 'Julio'
idade = 24
cidade = 'Belo Horizonte'

print(f'O {nome} tem {idade} anos de idade e mora em {cidade}.')'
'''
'''
# Adicionando Input
nome = input('Digite o seu nome: ')
idade = int(input('Digite a sua idade: '))
cidade = input('Digite a sua cidade: ')

print(f'O {nome} tem {idade} anos de idade e mora em {cidade}.')'
'''
'''
# Calculando a idade com Input
ano_nascimento = int(input('Digite o ano do seu nascimento: '))
idade = int(input('Digite o ano atual: '))
idade = idade - ano_nascimento

print(f' Você tem {idade} anos de idade.')'
'''
'''
# Entendendo o Slice
# Slice é uma forma de selecionar partes de uma string.

fruta = 'Abacate'
# index = 0123456 (Posição de cada letra)
print(fruta[3]) # imprime somente a letra "c"
print(fruta[0:3]) # imprime somente as letras "aba"
print(fruta[3:]) # imprime somente as letras "cete"
print(fruta[-1]) # imprime somente a letra "e" porque conta de tras para frente

valor = 99.75
valor = str(valor)
print(valor[2:]) imprime do ponto ate o final "75"
'''
'''
# Utilizando Formated Strings
# O Marcos Silva é um excelente [Programador].

nome = 'Marcos' 
sobrenome = 'Silva'
profissao = 'Programador'

texto = 'O ' + nome + ' ' + sobrenome + ' é um excelente [' + profissao + '].' # Sem Formated Strings
print(texto)

texto2 = f'O {nome} {sobrenome} é um excelente [{profissao}].' # Com Formated Strings
print(texto2)
'''

# Metodos para Strings

mensagem = 'Eu adoro comida caseira!'
print(mensagem.upper()) # Transforma todas as letras em maiusculas
print(mensagem.lower()) # Transforma todas as letras em minusculas
print(mensagem.capitalize()) # Transforma a primeira letra em maiuscula
print(mensagem.title()) # Transforma a primeira letra de cada palavra em maiuscula
print(mensagem.split()) # Separa as palavras em uma lista
print(mensagem.replace('comida', 'jogos')) # Substitui uma palavra por outra
print(mensagem.find('comida')) # Encontra a posição da palavra
print(len(mensagem)) # Conta a quantidade de caracteres
print(mensagem.count('a')) # Conta a quantidade de letras
print(mensagem.strip()) # Remove os espaços em branco
