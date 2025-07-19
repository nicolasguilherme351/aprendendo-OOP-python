import classeUsuario

usuario = classeUsuario.Usuário("Pedro", 19, "q11243")

print("Este é o nome do usuário: " + usuario.nome)
print("Este é a idade do usuário:", usuario.verIdade())

# Não se consegue ver a senha usuário, e não há método que mostre-a.