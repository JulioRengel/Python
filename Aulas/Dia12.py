
# Erros 
    # Excelentes para testes 
    # Não realizan o 'stop' no programa
    # Mensagens customizadas quando encontra um erro

'''
# Trabalhando com Try e Exept com uma lista

try:
    letras = ['a', 'b', 'c']
    print(letras[3])
except IndexError:
    print('Index não existe')


# Trabalhando com Try e Except com input

try:
    valor = int(input('Digite o valor do seu produto: '))
    print(valor)
except ValueError:
    print('Favor digitar um valor em numeros')
'''

# Adicionando Else e Finally

try:
    valor = int(input('Digite o valor do seu produto: '))
    print(valor)
except ValueError:
    print('Favor digitar um valor em numeros')
finally:
    print('Codigo ok')


'''
else:
    print('Usuario digito um valor correto')
    resultado = valor * 2
    print(resultado)
'''