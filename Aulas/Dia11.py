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

'''
#Looping dentro de uma lista

valores =  [50, 80, 110, 150, 170]

for x in valores:
    print(f' O valor final do produto é de R$ {x}')
'''
'''
# Verificando itens em uma lista

corCliente = input('Digite a cor desejada: ')
cores = ['amarelo', 'verde', 'azul', 'vermelho']

if corCliente.lower() in cores: #lower() detecta escrita em maiuscula e minuscula
    print('Em estoque')
else:
    print('Não temos esta cor em estoque')
'''
'''
# Agregando duas listas com o Zip

cores = ['amarelo', 'verde', 'azul', 'vermelho']
valores = [10, 20, 30, 40]

duasListas = zip(cores, valores)

print(list(duasListas))
'''
'''
# Input em uma lista 
frutasUsuario = input('Digite o nome das frutas separados por virgula: ')
frutasLista = frutasUsuario.split(', ')
print(frutasLista)
'''
'''
# Entendendo sobre Tuples

coresList = ['amarelo', 'verde', 'azul', 'vermelho']
coresTuples = ('amarelo', 'verde', 'azul', 'vermelho')

print(type(coresList))
print(type(coresTuples))
'''
'''
# Trabalhando com Arrays 
    # Arrays (Matriz)
    # Melhor performance
from array import array
letras = ['a', 'b', 'c', 'd']
numeros_i = [10, 20, 30, 40]
numeros_f = [1.2, 2.2, 3.2]

print(letras)
print(numeros_i)
print(numeros_f)

letras = array('u', ['a', 'b', 'c', 'd'])
numeros_i = array('i', [10, 20, 30, 40])
numeros_f = array ('f', [1.2, 2.2, 3.2] )

print(letras)
print(numeros_i)
print(numeros_f)
'''
'''
# Criando Sets
    #Set (Listas)
    #Evita itens duplicados
    #Não utiliza index 

list1 = [10, 20, 30, 40, 50]
list2 = [10, 20, 60, 70]

num1 = set(list1)
num2 = set(list2)

print(num1 | num2) # operador |(Union): une as duas lista e retira os repetidos.
print(num1 -  num2) # operador - (Difference): gera duas lista excluindo os numeros repetidos.
print(num1 ^ num2) # operador ^ (Symmetric Difference): gera duas lista e tira os numeros duplicados.
print(num1 & num2) # operador & (and): gera uma lista só com os numeros repetidos. 

print(len(list1)) # permite ver a cantidade de intens contida na lista. 
'''
'''
# Funções em Sets
    #Similar a listas
    #Evita itens duplicados
    #Não utiliza index 

# list1 = [1, 2, 3, 4, 5, 6]
s1 = {1, 2, 3, 4, 5, 6, 2}
s1.add(4)
s1.update([7, 8, 9])
s1.remove(9) #Gera erro quando o numero não esta na lista
s1.discard(8)# não gera erro quando o numero não este na lista.
# print(list1)
print(s1)
# print(type(list1))
#print(type(s1))
'''
'''
#Sets com strings

set1 = {'a', 'b', 'c'}
set2 = {'a', 'd', 'e'}
set3 = {'c', 'd', 'f'}

# set4 = set1.union(set2)
# set4 = set1.difference(set3)
# set4 = set1.intersection(set2)
set4 = set1.symmetric_difference(set3)

print(set4)
'''
#Introdução a Dicionarios. 
    # Utiliza o index no formato Keys e Values
    # Aceita string, integer, float, boolean...

aluno = {'nome': 'ana', 'idade': 16, 'nota final': 'A', 'aprovação': True}

print(aluno)