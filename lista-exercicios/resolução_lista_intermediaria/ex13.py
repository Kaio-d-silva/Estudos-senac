# Função para ler uma lista de 10 números inteiros
def ler_lista():
    numeros = []
    for i in range(10):
        while True:
            try:
                num = int(input(f"Digite o {i+1}º número inteiro: "))
                numeros.append(num)
                break
            except ValueError:
                print("Por favor, insira um número inteiro válido.")
    return numeros

# Função para calcular a soma e a média dos números


def calcular_soma_media(numeros):
    soma = sum(numeros)
    media = soma / len(numeros)
    return soma, media


# Programa principal
numeros = ler_lista()
soma, media = calcular_soma_media(numeros)

print(f"\nA soma dos números é: {soma}")
print(f"A média dos números é: {media:.2f}")