# Função Lambda
    # É uma função pequena sem nome
    # Pode ter varios argumentos mas só uma expresão
    # Muito utilizada dentro de outras funções 
    # Código mais 'clean'

# def somar (x):
    # return x + 10

# print(somar(2))

somar10 = lambda x,y: x + y + 10

print(somar10(2,4))