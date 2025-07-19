class Usuário():
    def __init__(self, nome, idade, senha):
        self.nome = nome 
        self.__idade = idade
        self.__senha = senha
    
    def verIdade(self):
        return self.__idade
    
