# Exercicio para praticar - Temperatura
temperatura = float(input('Digite a temperatura atual: '))
if temperatura < 10:
    print('Está muito frio!')
elif temperatura >= 10 and temperatura < 20:
    print('Está fresco!')
else:
    print('Está quente!')