def calcular_anos():
    while True:
        try:
            populacao_a = float(input("Digite a população do país A: "))
            taxa_a = float(input("Digite a taxa de crescimento do país A (em %): "))
            populacao_b = float(input("Digite a população do país B: "))
            taxa_b = float(input("Digite a taxa de crescimento do país B (em %): "))
            if populacao_a <= 0 or populacao_b <= 0 or taxa_a < 0 or taxa_b < 0:
                print("Erro: As populações e taxas de crescimento devem ser positivas.")
                continue
            anos = 0
            while populacao_a < populacao_b:
                populacao_a = populacao_a * (1 + taxa_a / 100)
                populacao_b = populacao_b * (1 + taxa_b / 100)
                anos += 1
            print(f"Serão necessários {anos} anos para que a população do país A ultrapasse ou iguale a população do país B.")
            resposta = input("Deseja repetir a operação? (s/n): ")
            if resposta.lower() != 's':
                break
        except ValueError:
            print("Erro: Entrada inválida. Por favor, digite um número.")

calcular_anos()