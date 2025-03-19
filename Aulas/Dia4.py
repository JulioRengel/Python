# A função INPUT() é utilizada para receber dados do usuário. O dado é sempre retornado como uma string.

#nome = input('Qual é o seu nome? ')
#julioprint(f'Olá, {nome}!')
# O código acima pede ao usuário para inserir o seu nome e, em seguida, imprime uma mensagem de saudação com o nome do usuário.

'''
# Criando uma sequencia de Inputs

nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')
pais_de_origem = input('Digite seu país de origem: ')

print(f'Olá, meu nome é {nome}, tenho  {idade} anos de idade, meu pais de origem é {pais_de_origem}.')
'''

'''
# Convertendo de string para Integer
nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: ')) # Convertendo a string para inteiro

print(type(nome))
print(type(idade))
'''

'''
# Criando um programa com o Input
valor_produto = float(input('Digite o valor do produto: R$ ')) # Captura o valor do produto

# Calcula o valor do produto com 10% de acrescimo
valor_com_acrescimo = valor_produto * 1.10

# exibir o valor final ma tela
print(f'O valor do produto com 10% de acrescimo é R$ {valor_com_acrescimo:.2f}')'
'''
'''
# Multiplas entradas na mesma linha de Input
dados = input('Digite seu nome, idade e país de origem: ').split() # Captura os dados e transforma em uma lista
nome = dados[0] # Atribui o primeiro elemento da lista a variavel nome
idade = dados[1] # Atribui o segundo elemento da lista a variavel idade
pais_de_origem = dados[2] # Atribui o terceiro elemento da lista a variavel pais_de_origem

print (f'Meu nome é {nome}, tenho {idade} anos de idade e meu pais de origem é {pais_de_origem}.')
'''

# Criando uma entrada fromatda
dados = input('Digite seu nome, idade e país de origem: ').split()
nome = dados[0]
idade = dados[1]
pais_de_origem = dados[2]

print (f'Meu nome é {nome.upper()}, tenho {idade} anos de idade e meu pais de origem é {pais_de_origem.upper()}.')