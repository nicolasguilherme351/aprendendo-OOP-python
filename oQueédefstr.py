# Pode ser comparado ao um toString em Java
# Função aoende é mostrado os atributos da classe

class Animal:
    def __init__(self, nome, cor):
        self.nome = nome 
        self.cor = cor 
        pass
    def __str__(self):
        return f"{self.nome}{self.cor}"
        pass


p1 = Animal("Nicolas", "Azul")

print(p1.nome)
print(p1.cor)