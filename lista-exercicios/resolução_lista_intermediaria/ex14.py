def ler_matriz(n):
    matriz = []
    for i in range(n):
        linha = []
        for j in range(n):
            while True:
                try:
                    elemento = int(input(f"Digite o elemento [{i+1},{j+1}] da matriz: "))
                    linha.append(elemento)
                    break
                except ValueError:
                    print("Por favor, insira um número inteiro válido.")
        matriz.append(linha)
    return matriz

def soma_matriz(matriz):
    soma = 0
    for linha in matriz:
        soma += sum(linha)
    return soma

def main():
    while True:
        try:
            n = int(input("Digite o tamanho N da matriz (N x N): "))
            if n > 0:
                break
            else:
                print("Por favor, insira um valor positivo para N.")
        except ValueError:
            print("Por favor, insira um número inteiro válido.")

    matriz = ler_matriz(n)
    soma = soma_matriz(matriz)

    print(f"\nA matriz inserida foi:")
    for linha in matriz:
        print(linha)

    print(f"\nA soma dos elementos da matriz é: {soma}")

if __name__ == "__main__":
    main()
