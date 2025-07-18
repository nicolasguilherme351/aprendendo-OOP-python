class Pessoa():
    def __init__(self, nome, idade):
        self.nome = nome 
        self.idade = idade 

    def falar(self): # self referencia a atual instancia da classe, e pode ser usado para acessar váriaveis da própria classe. 
        print("Olá! ") 


    def pensar(self):
        return "a"

pessoa = Pessoa("Maria ", 23)

pessoa.falar()
print(pessoa.pensar())