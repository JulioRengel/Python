nota = float(input('Digite a nota do aluno: '))
if nota >= 9:
    print('Eexcelente! Você tirou um A!')
elif nota >= 7:
    print('Bom trabalho! Você tirou um B!')
elif nota >= 5:
    print('Você passou, mas precisa melhorar. Sua nota é C!')
else:
    print('Você foi reprovado.')