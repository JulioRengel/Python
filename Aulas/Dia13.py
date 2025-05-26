from datetime import datetime

# Python Object-Oriented Programming

# Classes 
    # Utilizadas para criar Objetos (instances)
    # Objetos são partes dentro de uma Class (instancias)
    # Classes são utilizadas para agrupar dados e funções, podendo reutilizar. 
    # ===
    # Class: Frutas
    # Objects: Abacate, Banana...
'''
# Criando nossa primeirea classe

class Funcionarios:
    nome = 'Elena'
    sobrenome = 'Cabral'
    dataNascimento = '15/07/1988'

usuario1 = Funcionarios ()

print(usuario1.nome)
print(usuario1.sobrenome)
'''
'''
# Criar classe
class Funcionarios:
   pass # faz com que a classe fique vazia. 

# Criar Objeto
usuario1 = Funcionarios ()
usuario2 = Funcionarios ()


# Criar os parametros do usuario1
usuario1.nome = 'Elena'
usuario1.sobrenome = 'Cabral'
usuario1.dataNascimento = '15/07/1988'

# Criar os parametros do usuario2
usuario2.nome = 'Sharly'
usuario2.sobrenome = 'Rengel'
usuario2.dataNascimento = '13/05/2020'

# Print

print(usuario1.nome)
print(usuario2.dataNascimento)
'''

# Criando Construtores: reduz a passagem de parametros. 
# Adicionando mais funções a classes
# Calculando a idade do funcionario

class Funcionarios:

    def __init__(self, nome, sobrenome, anoNascimento):
             self.nome = nome
             self.sobrenome = sobrenome
             self.anoNascimento = anoNascimento
    def nomeCompleto(self):
           return self.nome + ' ' + self.sobrenome

    def idadeFuncionario(self):
           anoAtual = datetime.now().year
           self.anoNascimento = int(anoAtual - self.anoNascimento)
           return self.anoNascimento

usuario1 = Funcionarios ('Elena', 'Cabral', 1988)
usuario2 = Funcionarios ('Sharly', 'Rengel', 2020)
usuario3 = Funcionarios ('Gary', 'Rengel', 2020)

print(Funcionarios.idadeFuncionario(usuario1))
print(Funcionarios.idadeFuncionario(usuario2))
print(Funcionarios.idadeFuncionario(usuario3))





