# Operadores de comparação
'''
a = 10
b = 20

print (a == b) # Verifica se a é igual a b
print (a != b) # Verifica se a é diferente de b
print (a > b) # Verifica se a é maior que b
print (a < b) # Verifica se a é menor que b
print (a >= b) # Verifica se a é maior ou igual a b
print (a <= b) # Verifica se a é menor ou igual a b

print (ord('a')) # Retorna o valor ASCII do caractere
print (ord('b')) # Retorna o valor ASCII do caractere
'''
'''
# Utilizando IF

idade = int(input('Digite sua idade: ')) # Captura a idade do usuário 

if idade >= 18:
    print('Maior de idade!')
'''
'''
# Utilizando ELSE

idade = int(input('Digite sua idade: ')) 

if idade >= 18:
    print('Maior de idade!')
else:
     print('Menor de idade!')
'''

# Utilizando ELSE IF

idade = int(input('Digite sua idade: '))
if idade < 18:
        print('Menor de idade!')
elif idade >= 18 and idade < 60:
        print('Maior de idade!')
else:
     print('Idoso')