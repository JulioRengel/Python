

# Desafio com funçoes

'''
Criar um programa que calcula a quantidade de tinta necessária para pintar uma parede. 
O usuario deverá fornecer as siguentes informaçoes: Rendimento, altura e largura. 

O programa deve mostrar na tela a mensagem 'Voce necesita x latas de tinta.

Qual é o rendimento da lata? 
Qual é a altura da pardede?
Qual é a largura da parede?
'''

def entradaInteira(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print('Erro: Por favor, digite um número inteiro.')

rendimento = entradaInteira ('Qual é o rendimento da lata? ')
altura = entradaInteira('Qual é a altura da pardede? ')
largura = entradaInteira ('Qual é a largura da parede? ')


def calculoTinta():
    area = altura * largura
    total = area / rendimento
    print('')
    print(f'Voce necesita de {total} latas de tinta.')

calculoTinta()