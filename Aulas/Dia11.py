# Introdução a Listas
# cidades = ['Rio de Janeiro', 'São Paulo', 'Salvador']
'''
# Manipulando Listas 

cidade1 = 'Rio de Janeiro'
cidade2 = 'São Paulo'
cidade3 = 'salvador'

cidades = ['Rio de Janeiro', 'São Paulo', 'Salvador', 'Goiania']

cidades [0] = 'Brasilia'
print(cidades)

# print(cidades[2])
# print(cidades[-4])
'''
'''
# Funçoes dentro de Listas

cidades = ['Rio de Janeiro', 'São Paulo', 'Salvador', 'Goiania']

cidades.append('Santa Catarina') #agrega el inten informado dentro del parentesis en la ultima posicion
cidades.remove('Salvador') #elimina el item de la lista informado en el párenteis
cidades.insert(1, 'Santa Catarina') #sustitui um item por outro. temq ue informar a posicion y el nombre que sera trocado. 
cidades.pop(0) # apaga el iten encontrado en la possicion informada em el parentesis. 
cidades.sort() #Organiza em ordem alfabetica.

print(cidades)
'''
'''
# Concatenando listas

numeros = [2, 3, 4, 5]
letras = ['a', 'b', 'c', 'd']

#final = numeros + letras
numeros.extend(letras)

print (numeros)

#lista dentro de listas

itens = [['itens1', 'itens2'] , ['itens3', 'itens4']]

print(itens[0][1])
'''
'''
# Extraindo Variaveis de listas

produtos = ['arroz', 'feijão', 'laranja', 'banana', 4, 5, 6, 7]

item1, item2, item3, *outros = produtos

print (item1)
print (item2)
print (item3)
print (outros)
'''


#Looping dentro de uma lista

valores =  [50, 80, 110, 150, 170]

for x in valores:
    print(f' O valor final do produto é de R$ {x}')
