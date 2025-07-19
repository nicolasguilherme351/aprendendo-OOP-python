# Polimorifismo é diferentes formas de executar o mesmo método dependendo do objeto.

class Pessoa(): 
    def __init__(self, nome, idade):
        self.nome = nome 
        self.idade = idade

    def falar(self):
        print("Olá")

class Estudante(Pessoa): 
    def __init__(self, nome, idade, curso):
        super().__init__(nome, idade)
        self.curso = curso 

    def falar(self): # Uma outra maneira de executar o mesmo método.
        print(f"Olá, eu estudo {self.curso}")        

pessoa = Pessoa("Pedro ", 16)
estudante = Estudante("Maria ", 16, "Administração")

pessoa.falar()
estudante.falar()

