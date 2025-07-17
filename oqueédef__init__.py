# O def __init__ permite que definamos os atributos da classe ao cria-la. Basicamente poderia ser comparado ao um funcionamento de um construtor

class Animal:
    def __init__(self, nome, cor):
        self.nome = nome 
        self.cor = cor 
        

p1 = Animal("Nicolas", "Azul")

print(p1.nome)
print(p1.cor)