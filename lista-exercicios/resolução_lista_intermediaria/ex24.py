def calcular_soma_e_media():
    numeros = []
    soma = 0

    for i in range(5):
        while True:
            try:
                numero = float(input(f"Digite o {i+1}º número: "))
                numeros.append(numero)
                soma += numero
                break
            except ValueError:
                print("Por favor, insira um número válido.")

    media = soma / len(numeros)
    return soma, media

# Programa principal
soma, media = calcular_soma_e_media()
print(f"A soma dos números informados é: {soma}")
print(f"A média dos números informados é: {media:.2f}")
8889