def verifica_senha():
    nome_usuario = str(input("Informe o nome de usario : "))
    senha_usuario = str(input("Informe a sua senha : "))
    if senha_usuario == nome_usuario:
        print("Senha invalida")
    else:
        return "sair"
    
saida = ""
while saida != "sair":
    saida = verifica_senha()

