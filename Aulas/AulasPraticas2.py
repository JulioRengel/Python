def potencia(base, exponente=2):
    return base ** exponente

userNumber = int(input('Digite o numero base: '))
userExponente = input('Digite um expoente (default 2): ')

if userExponente: 
    print(f'O resultado é: {potencia(userNumber, int(userExponente))}')

else:
    print(f'O resultado é: {potencia(userNumber)}')