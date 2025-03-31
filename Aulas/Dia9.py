'''
# If, Else

velocidade = 120

if velocidade > 110: 
    print(f'Acima da Velocidade Permitida')
    print(f'Por favor, reduzir a sua velocidade')
elif velocidade < 60:
    print(f'Por favor, dirigir acima de 80km/h')

else:
    print(f'Velocidade OK')
'''
'''
# Operadores Lógicos

rendaPerCapita = True
estusFinanceiro = False

# if rendaPerCapita and estusFinanceiro:
if rendaPerCapita or estusFinanceiro:
    print(f'Financiamento Aprovado')

else:
    print(f'Financiamento Negado')
'''
'''
# Multiplos Operadores de Comparação

valor = 25

# if valor >= 20 and valor < 40:
if 20 <= valor < 40:
    print(f'Produto foi Aceito')

else:
    print('Produto não Ceito')'
'''
'''
# For Loop - Utilizando números

# Imprimindo de 1 a 5.

for numero in range (1,5):
    print(numero)
'''
'''
# For Loop - Utilizando Strings
palavra =  'Rodrigo'

for letra in palavra:
    # print(letra)
    # print(letra + ' Esta dentro da palavra Google')

    print(f'{letra} Esta dentro da palavra {palavra}')
'''

# For Loop - Utilizando If e Else

