def gerar_intervalo_e_somar(numero1, numero2):
    soma = 0
    if numero1 < numero2:
        for i in range(numero1 + 1, numero2):
            print(i)
            soma += i
    elif numero1 > numero2:
        for i in range(numero2 + 1, numero1):
            print(i)
            soma += i
    else:
        print("Os números são iguais, não há intervalo.")
        return 0
    
    return soma

# Programa principal
try:
    numero1 = int(input("Digite o primeiro número inteiro: "))
    numero2 = int(input("Digite o segundo número inteiro: "))
    print(f"Números inteiros no intervalo entre {numero1} e {numero2}:")
    soma = gerar_intervalo_e_somar(numero1, numero2)
    if soma != 0:
        print(f"\nA soma dos números no intervalo é: {soma}")
except ValueError:
    print("Por favor, insira números inteiros válidos.")
1