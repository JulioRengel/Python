'''
# Exercicio para praticar - Temperatura
temperatura = float(input('Digite a temperatura atual: '))
if temperatura < 10:
    print('Está muito frio!')
elif temperatura >= 10 and temperatura < 20:
    print('Está fresco!')
else:
    print('Está quente!')
'''
'''
# Exercicio para praticar - Saudações
from datetime import datetime
horario = input('Digite o horário atual: ')
horario = datetime.strptime(horario, '%H:%M')
if horario >= datetime.strptime('00:00', '%H:%M') and horario < datetime.strptime('12:00', '%H:%M'):
    print('Bom dia!')
elif horario >= datetime.strptime('12:00', '%H:%M') and horario < datetime.strptime('18:00', '%H:%M'):
    print('Boa tarde!')
else:
    print('Boa noite!')
'''
'''
# Exercicio para praticar - Desconto
valor_compra = float(input('Digite o valor da compra: R$ '))
if valor_compra < 100:
    desconto = valor_compra * 0.05
    print(f'O valor da compra com desconto é R$ {valor_compra - desconto:.2f}')
elif valor_compra >= 100 and valor_compra < 200:
    desconto = valor_compra * 0.10
    print(f'O valor da compra com desconto é R$ {valor_compra - desconto:.2f}')
else:
    desconto = valor_compra * 0.20
    print(f'O valor da compra com desconto é R$ {valor_compra - desconto:.2f}')
'''
'''
# Exercicio para praticar - Login
usuario_1 = 'admin'
senha_1 = '123456'

usuario = input('Digite o seu nome de usuário: ')
senha = input('Digite o seu nome de usuário: ')

if usuario == usuario_1 and senha == senha_1:
    print ('Login efetuado com sucesso!')
else:
    print('Usuário ou senha incorretos!')
'''

# Exercicio para praticar - Desempenho

nota = float(input('Digite a nota do aluno: '))
if nota >= 9:
    print('Eexcelente! Você tirou um A!')
elif nota >= 7:
    print('Bom trabalho! Você tirou um B!')
elif nota >= 5:
    print('Você passou, mas precisa melhorar. Sua nota é C!')
else:
    print('Você foi reprovado.')
    