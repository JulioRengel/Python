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