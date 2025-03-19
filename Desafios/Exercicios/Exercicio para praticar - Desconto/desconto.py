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