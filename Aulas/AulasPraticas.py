

'''
numero = 1

while numero <= 10:
    print(numero)
    numero += 1

print ('Loop com Break: ')
for numero in range(1,11):
    if numero > 5:
        break
    print(numero)


print ('Loop com Continue: ')
for numero in range(1,11):
    if numero == 5:
        continue
    print(numero)
'''
'''
frutas = ['maça', 'manga', 'banana', 'maça', 'mexirica', 'maça']
contador = 0

for fruta in frutas:
    if fruta == 'maça':
        contador += 1


print('Numero de maças na lista: ', contador)
'''

'''
numero = int(input('Digite um numero: '))

if numero > 10:
    print('O número é maior que 10')
else:
    print('O número é menor ou igual a 10')
'''
'''
idade = int(input('Digite sua idade: '))

if idade < 13:
    print('Você é uma criança!')
elif idade <= 19:
    print('Você é um adolescente!')
else:
    print('Você é adulto!')
'''
'''
carrosEmEstoque = ['BMW X6', 'BMW i5', 'BMW i8' ]
carro = input('Digite o nome do veiculo que deseja comprar: ')

if carro in carrosEmEstoque:
        print('Este carro está disponível')
else:
    print('Desculpe, este carro não está disponível')
'''
'''
while True:
    fruta = input('Adivine o nome da fruta: ')
    if fruta.lower() == 'abacate':
        break
print('Parabéns, você acertou a fruta!')
'''
'''
# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros = list(range(1,11))

for num in numeros:
    if num % 2 == 0:
        print(f'O número {num} é par!')
    else:
        print(f'O número {num} é ímpar!')
'''
'''
cidades = ('Belo Horizonte', 'São Paulo', 'Rios de Janeiro' )
cidadeUsuario = input('Digite o nome da sua cidade:')

if cidadeUsuario in cidades:
    print('A cidade esta na lista de cidades.')
else:
    print('A cidade não esta na lista de cidades.')
'''
'''
capitais = {
    'Brasil': 'Brasília',
    'Argentina': 'Buenos Aires',
    'Venezuela': 'Caracas',
    'Australia': 'Canberra',
    'Canada': 'Ottawa'
}

paisUsuario = input('Digite o nome do País:')

if paisUsuario in capitais:
    print(f'A capital de {paisUsuario} é {capitais[paisUsuario]}')
else:
    print('Desculpe, não temos informaçoes dobre a capital desse país.')
'''
'''
amigos1 = {'Luis', 'Carlos', 'Maria', 'Sharly', 'Gary'}
amigos2 = {'Luisa', 'Sharly', 'Gary', 'Maria', 'Stefania'}

amigos3 = amigos1.__and__(amigos2)

print(amigos3)
'''
'''
def quadrado(numero):
    return numero ** 2

num = int(input('Digite um numero: '))

print(f'O quadrado de {num} é {quadrado(num)}')
'''

def soma(num1, num2):
    return num1 + num2
    # print(f'A soma dos dois numeros é igual a: {result}')

userNum1 = int(input('Digite o primeiro numero: '))
userNum2 = int(input('Digite o segundo numero: '))

print(f'A soma dos dois numeros é igual a: {soma(userNum1, userNum2)}')