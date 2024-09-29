def pedir_usuario_senha():
    while True:
        usuario = input("Digite o nome de usuário: ")
        senha = input("Digite a senha: ")
        if senha != usuario:
            return usuario, senha
        else:
            print("Erro: A senha não pode ser igual ao nome de usuário. Tente novamente.")

# Exemplo de uso
usuario, senha = pedir_usuario_senha()
print(f"Usuário e senha registrados com sucesso!")
