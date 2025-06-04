

# Desafio com 'Sets'

'''
Criar um programa que gera 3 listas de acordo com anecessidade logo abaixo:

Lista1 = Funcionarios que tem carro e trabalhan de noite.
Lista2 = Funcionarios que tem carro e trabalhan durante o dia.
Lista3 = Funcionarios que não tem carro.
'''

funcionarios = {'Ana', 'Marcos', 'Alice', 'Pedro', 'Sophia', 'Bruno', 'Melissa'}
turnoDia = {'Ana', 'Marcos', 'Alice', 'Melissa'}
turnoNoite = {'Pedro', 'Sophia', 'Bruno'}
temCarro = {'Marcos', 'Alice', 'Bruno', 'Melissa'}

lista1 =  turnoNoite.intersection (temCarro)
print('Funcionarios que tem carro e trabalhan de noite: ', lista1)

lista2 =  turnoDia.intersection (temCarro)
print('Funcionarios que tem carro e trabalhan durante o dia: ', lista2)

lista3 =  funcionarios.symmetric_difference (temCarro)
print('Funcionarios que não tem carro: ', lista3)


'''
# Solução do professor.
funcionarios = {'Ana', 'Marcos', 'Alice', 'Pedro', 'Sophia', 'Bruno', 'Melissa'}
turno_dia = {'Ana', 'Marcos', 'Alice', 'Melissa'}
turno_noite = {'Pedro', 'Sophia', 'Bruno'}
tem_carro = {'Marcos', 'Alice', 'Bruno', 'Melissa'}

lista1 = set(tem_carro).intersection(turno_noite)
print(lista1)

lista2 = set(tem_carro).intersection(turno_dia)
print(lista2)

lista3 = set(funcionarios).difference(tem_carro)
print(lista3)

'''