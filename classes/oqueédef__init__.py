# O def __init__ permite que definamos os atributos da classe ao cria-la. Basicamente poderia ser comparado ao um funcionamento de um construtor

class Animal:
    def __init__(self, nome, cor):
        self.nome = nome 
        self.cor = cor 
        
p1 = Animal("Nicolas", "Azul")
a = 3/3
print(p1.nome)
print(p1.cor)
booster =  f"{p1} tudo que está frequentemetbne "