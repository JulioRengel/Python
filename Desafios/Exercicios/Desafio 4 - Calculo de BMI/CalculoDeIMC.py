

# Calculo de IMC - Indice de Massa Corporal. 

'''
Qual é sua Altura em cm: 
Qual é seu peso em kg: 

* MENOR QUE 18,5 --> MAGREZA
* ENTRE 18,5 E 24,9 --> NORMAL
* ENTRE 25,0 E 29,9 --> SOBREPESO
* ENTRE 30,0 E 39,9 --> OBESIDADE
* MIOR QUE 40,0 OBESIDADE GRAVE
'''

def entradaDecimal(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print('Erro: Por favor, digite um número com decimais, substituindo a vírgula pelo ponto.')

altura = entradaDecimal ('Qual é sua Altura em cm: ')
peso = entradaDecimal ('Qual é seu peso em kg: ')

def calculoImc(peso, altura):
    imc = peso / (altura ** 2)
    print(f'Seu IMC é: {imc: .2f}' )
    return imc

imc = calculoImc(peso, altura)

if imc > 40.0:
    print('Obesidade Grave')
elif imc >= 39.9: 
    print('Obesidade')
elif imc >= 29.9:
    print('Sobrepeso')
elif imc >= 24.9:
    print('Normal')
else:
    print('Magreza')


'''
# Solução do profesor

altura =  float(input('Qual é sua Altura em cm: '))
peso = float(input('Qual é seu peso em kg: '))

IMC = peso / (altura/100)** 2

if IMC < 18.5:
    print('Magreza')
elif IMC >= 18.5 and IMC < 24.9:
    print('Normal')
elif IMC >= 25.0 and IMC < 29.9:
    print('Sobrepeso')
elif IMC >= 30.0 and IMC < 39.9:
    print('Obesidade')
else:
    print('Obesidade Grave')
'''