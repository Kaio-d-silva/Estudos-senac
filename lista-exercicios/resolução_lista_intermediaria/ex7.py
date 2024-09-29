def soma_maior_menor():
    numeros = []
    for i in range(10):
        numeros.append(int(input(f"Digite o número {i+1}: ")))
    soma = sum(numeros)
    maior = max(numeros)
    menor = min(numeros)
    print(f"Soma: {soma}")
    print(f"Maior: {maior}")
    print(f"Menor: {menor}")

soma_maior_menor()