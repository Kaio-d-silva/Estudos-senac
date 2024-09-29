def encontrar_maior():
    maior = None  # Inicializa a variável para armazenar o maior número

    for i in range(5):
        while True:
            try:
                numero = float(input(f"Digite o {i+1}º número: "))
                break
            except ValueError:
                print("Por favor, insira um número válido.")

        if maior is None or numero > maior:
            maior = numero

    return maior


# Programa principal
maior_numero = encontrar_maior()
print(f"O maior número informado foi: {maior_numero}")
