# Pode ser comparado ao um toString em Java
# Função aoende é mostrado os atributos da classe

class Pessoa:
    def __init__(self, nome, idade, altura):
        self.nome = nome # Pode ser visto e modificado por essa classe, por outras classes, e por qualquer outro programa;
        self._idade = idade # Indica que pode ser visto, modificado e deletado por essa classe e subclasses;
        self.__altura = altura # Apenas pode ser visto, modificado e deletado por essa classe.

    def verAltura(self):
        return self.__altura
       
p1 = Pessoa("Pedro", 19, 1.70)

print(p1.nome) # atributo púlblico 
print(p1._idade) # atributo protegido, pode ser mudado mas não é recomendado
print(Pessoa.verAltura(p1)) # atributo privado podendo ser visto pela classe Pessoa

p1.nome = 3 
p1._idade = 4 
p1.__altura = 1.64 # Não modifica

print(p1.nome)
print(p1._idade)
print(p1.verAltura()) 

del p1.nome
del p1._idade
del p1.__altura # Não deleta

print(p1.verAltura()) 
