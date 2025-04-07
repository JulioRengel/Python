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
'''
# For Loop - Utilizando If e Else

# Enviar um e-mail com os detalhes da compra online (MAximo 3 tentativas) para compras comfirmadas. 

compraConfirmada = True
dadosCompra = 'Compra no valor de R$ 12.50 e entrega confirmada'

for enviar in range(3):
    if compraConfirmada:
        print(dadosCompra)
        print('Detalhes enviado pa seu e-mail')
        break
else:
    print('Falha na compra')
'''
'''
# For Loop - Nested Loops
# Outer loop (loop de fora)
# Inner loop (loop de dentro)

for numero1 in range(5):
    print(numero1)
    for numero2 in range(5):
        print(numero1, numero2)
'''
'''
# For Loop - Separando Strings

# Modificando FANTASTICO para F A N T A S T I C O 

palavra = 'FANTASTICO'

for spaco in palavra:
    print(f' {spaco}', end=' ')
'''
'''
# For Loop - Criando um Retangulo

linhas = 6
colunas = 6
simbolo = '|'

for l in  range(linhas):
    for c in range(colunas):
        print(simbolo, end='')
    print()
'''
'''
# == Conhecendo o While Loop ===
# Excelente para loops dependentes de uma condição
# Criar uma prmoção para um produto no valor de R$ 100,00
valor = 100
dia = 0

while valor > 20:
    dia += 1
    print(f' no dia {dia} o produto será vendido por: R$ {valor}')
    valor -= 5
'''
'''
# Operador Ternário

idade = 14

resultado = 'Voto permitido' if idade >= 16 else 'Voto não permitido'

print (resultado)
'''

# Criando condiçoes com While Loop
# Publicar um produto com comissão de 10% se for acim a de R$ 20

valor = float(input('Digite o valor do seu produto em R$: '))

while valor > 20: 
    valor = (valor * 0.10) + valor
    print(f'O valor do final do seu prduto será de R$ {valor: .2f}')
    break
