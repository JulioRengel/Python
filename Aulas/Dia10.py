# Como funciona uma função
    # DRY - Don't repeat yourself == Função foi feita para voce não se estar repetindo. 
'''
def boasVindas(): 
    print('Olá Marcos')
    print('Temos 5 laptops em estoque')

boasVindas()

print('Olá Nome')
print('Olá Nome')
print('Olá Nome')

boasVindas()
'''
'''
# Criando função de soma

def somarDoisNumeros():
    numero1 = 10
    numero2 = 5
    resultado = numero1 + numero2
    print(resultado)


somarDoisNumeros()
'''
'''
# PArametros e Argumetos em um a função

def boasVindas(nome, quantidade):
    print(f'Olá {nome}.')
    print(f'Temos {str(quantidade)} laptops em estoque')

boasVindas ('Ruben', 5)
boasVindas ('Carlos', 4)
boasVindas ('Ricardo', 2)


def boasVindasRuben():
    print('Olá Ruben')
    print('Temos 5 laptops em estoque')


def boasVindasCarlos():
    print('Olá CArlos')
    print('Temos 4 laptops em estoque')


def boasVindasRicardo():
    print('Olá Ricardo')
    print('Temos 2 laptops em estoque')


boasVindasRuben()
boasVindasCarlos()
boasVindasRicardo()
'''
'''
#Argumetos Default e Non-default
#Default = Aquele que voce define o valor no parametro. 
#Non-default = Aquele qie voce não define o valor nó parametro. 

def boasVindas(nome, quantidade=6):
    print(f'Olá {nome}.')
    print(f'Temos {str(quantidade)} laptops em estoque')

boasVindas ('Ruben', 5)
'''
'''
#Print ou Return em Funçoes
#Funções 
    #Realizan uma tarefa. 
    #Calcula e retorna um valor. 

def cliente1(nome):
    print(f'Olá {nome}')

def cliente2(nome):
    return f'Olá {nome}'

cliente1('Maria')

print(cliente2('Jose'))
'''
'''
#Varios argumetos xargs com numeros

def soma(*numeros):
    resultado = 0
    for num in numeros:
        resultado += num
    return resultado

x = soma(2,3,4,7)

print (x)
'''
'''
#Varios argumentos xargs nomenado parametros

def agencia (**carro):
    return carro


print(agencia(Marca = 'Gol',Cor = 'Branca', Motor = 1.0))
print(agencia(Marca = 'Gol',Cor = 'Branca', Motor = 1.0))
print(agencia(Marca = 'Gol',Cor = 'Branca', Motor = 1.0, Placa = 'AML-4568'))
'''

#Importando um Modulo
#¿ Qual é o numero fatorial de 4?
    # 4 * 3 * 2 * 1 = 24

import math

print(math.factorial(4))