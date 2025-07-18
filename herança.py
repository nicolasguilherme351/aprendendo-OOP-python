# Basicamente herança em OOP significa que uma classe herda todos os atributos e métodos de uma classe especifica. 

class Pessoa():
    def __init__(self, nomeDaPessoa, idadeDaPessoa):
        self.nomeDaPessoa = nomeDaPessoa
        self.idadeDaPessoa = idadeDaPessoa
        pass

    def falar(self): # O robo não fala. Mas isso será posteriormente resolvido com o polimorfismo.
        print("Olá")

class Robo(Pessoa):
      def __init__(self, nomeRobo, idadeRobo, material):
        super().__init__(nomeRobo, idadeRobo)
        self.material = material

robo = Robo("T-223", 123, "Bronze")

robo.falar()

