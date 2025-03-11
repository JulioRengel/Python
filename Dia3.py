'''
#Os detalhes de uma String
mensagem = 'Este curso é muito bom!' # Aspas simples impede a quebra de linha
mensagem2 = """
olá Aluno, 
Este curso é completo e tem tudo o quer você precisa 
para aprender Python.
""" # Aspas triplas permite a quebra de linha
print(mensagem2)

#Indexação Fatiamento
print(mensagem[0:4])
'''
'''
#Metodos comuns para Strings

mensagem = 'Este curso é muito bom!'

print(mensagem.upper()) # Deixa a string em maiusculo
print(mensagem.lower()) # Deixa a string em minusculo
print(mensagem.strip()) # Remove os espaços em branco
print(mensagem.replace('bom', 'maravilhoso')) # Substitui uma palavra por outra
print(mensagem.split()) # Transforma a string em uma lista
'''

'''
#Utilizando a f-string
nome = 'Maria'
idade = 30

print('O meu nome é ' , nome ,' e eu tenho ' , idade ,' anos.')
print(f'O meu nome é {nome} e eu tenho {idade} anos.')
'''

#adicionando Sequencias de Escape

# mensagem = 'Aprender Pytho é muito simples' # /n quebra de linha
# mensagem = 'Coluna1\tColuna2\tColuna3' # \t tabulação
# mensagem = 'c:\\Users\\Desktop\\Python' # \\ barra invertida
mensagem = 'Aprender \'Python\' é muito divertido!'
print(mensagem)

#Tabulação e unicode com Strings
mensagem = 'Nome:\tMaria Rodriguez\nIdade:\t30\nPais:\tBrasil'

#Caracteres Unicode
mensagem2 = 'Coração: \u2764'
print(mensagem)
print(mensagem2)