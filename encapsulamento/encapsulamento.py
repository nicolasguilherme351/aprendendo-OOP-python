# Basicamente esconder certos atributos de uma classe e expor eles apenas quando for necessário.

class Conta():
    def __init__(self, nome, saldo, senha):
        self.nome = nome
        self.__saldo = saldo
        self.__senha = senha

    def ver_saldo(self):
        return self.__saldo

conta = Conta("Pedro ", 1000, "1234")

print(conta.ver_saldo())

