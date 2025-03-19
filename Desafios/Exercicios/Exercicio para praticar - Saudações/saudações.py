from datetime import datetime
horario = input('Digite o horário atual: ')
horario = datetime.strptime(horario, '%H:%M')
if horario >= datetime.strptime('00:00', '%H:%M') and horario < datetime.strptime('12:00', '%H:%M'):
    print('Bom dia!')
elif horario >= datetime.strptime('12:00', '%H:%M') and horario < datetime.strptime('18:00', '%H:%M'):
    print('Boa tarde!')
else:
    print('Boa noite!')