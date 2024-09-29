def gerar_intervalo(numero1, numero2):
    if numero1 < numero2:
        for i in range(numero1 + 1, numero2):
            print(i)
    elif numero1 > numero2:
        for i in range(numero2 + 1, numero1):
            print(i)
    else:
        print("Os números são iguais, não há intervalo.")

# Programa principal
try:
    numero1 = int(input("Digite o primeiro número inteiro: "))
    numero2 = int(input("Digite o segundo número inteiro: "))
    print(f"Números inteiros no intervalo entre {numero1} e {numero2}:")
    gerar_intervalo(numero1, numero2)
except ValueError:
    print("Por favor, insira números inteiros válidos.")
