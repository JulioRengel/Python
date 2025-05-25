from sys import getsizeof

'''
# Função Lambda
    # É uma função pequena sem nome
    # Pode ter varios argumentos mas só uma expresão
    # Muito utilizada dentro de outras funções 
    # Código mais 'clean'

# def somar (x):
    # return x + 10

# print(somar(2))

somar10 = lambda x,y: x + y + 10

print(somar10(2,4))
'''

'''
# Lambda dentro de uma função

def somar(x):
    func2 = lambda x: x+ 10
    return func2(x) * 4

print(somar(2))
'''

'''
# Função Map em uma lista
    # Muito utilizada com listas.
    # Aplicar uma função a um Interable, por item. (list, tuple, dicionario, etc)

lista1 = [1, 2, 3, 4]

def multi(x):
    return x * 2

lista2 = map(multi, lista1)

print(list(lista2))
'''
'''
# Função Map em uma lista.

lista1 = [1, 2, 3, 4]

# lista2 = map(lambda x: x * 2, lista1)

print(list(map(lambda x: x * 2, lista1)))
'''
'''
# Função Filter

valores = [10, 12, 34, 44, 57]

def remover20(x):
    return x > 20

print(list(filter(remover20, valores)))

print(list(filter(lambda x: x > 20, valores)))
'''

'''
# Entendendo List Comprehension com Strings
    # Mas simples de se escrever
    # Utilizado quando voce precisa criar uma lista a partir de uma existente
    # [expressao for iten in itens]

frutas1 = ['abacate', 'banana', 'morango', 'kiwi', 'abacaxi']
# frutas2 = []

# for iten in frutas1: 
    # if  'b' in iten:
        # frutas2.append(iten)

frutas2 = [iten for iten in frutas1 if 'n' in iten]

print(frutas2)
'''
'''
# Entendendo List Comprehension com números

# valores = []

# for x in range(6):
    # valores.append(x * 10)

# print(valores)

valores = [x * 10 for x  in range(6)]
print(valores)
'''


# Listas e Gerator Expressions
    # Uma forma mas rápida para listas, diccionarios, etc. 
    # Menos memoria alocada.
    # Valores em Bytes. 

numeros = [x * 10 for x in range(10)]
print(type(numeros))
print(numeros)
print(getsizeof(numeros))

numeros = (x * 10 for x in range(10))
print(type(numeros))
print(list(numeros))
print(getsizeof(numeros))