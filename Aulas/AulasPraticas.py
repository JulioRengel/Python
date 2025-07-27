

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
idade = int(input('Digite sua idade: '))

if idade < 13:
    print('Você é uma criança!')
elif idade <= 19:
    print('Você é um adolescente!')
else:
    print('Você é adulto!')
