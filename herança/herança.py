# Basicamente herança em OOP significa que uma classe herda todos os atributos e métodos de uma classe especifica. 

class Pessoa():
    def __init__(self, nomeDaPessoa, idadeDaPessoa):
        self.nomeDaPessoa = nomeDaPessoa
        self.idadeDaPessoa = idadeDaPessoa
        pass

    def falar(self): # O robô não fala. Mas isso será posteriormente resolvido com o polimorfismo.
        print("Olá")
        if (len(self.nomeDaPessoa) >= 6): 
            print("Essa pessoa tem um nome com pelo menos 6 caracteres. ")

class Robô(Pessoa):
      def __init__(self, nomeRobô, idadeRobô, material): # Os atributos do Robô + os atributos da Pessoa.
        super().__init__(nomeRobô, idadeRobô) 
        self.material = material

robô = Robô("T-223", 123, "Bronze")

robô.falar()
