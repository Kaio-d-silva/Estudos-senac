def contar_pares_impares():
    pares = 0
    impares = 0

    for i in range(10):
        while True:
            try:
                numero = int(input(f"Digite o {i+1}º número inteiro: "))
                break
            except ValueError:
                print("Por favor, insira um número inteiro válido.")
        
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1

    return pares, impares

# Programa principal
pares, impares = contar_pares_impares()
print(f"\nQuantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {impares}")
