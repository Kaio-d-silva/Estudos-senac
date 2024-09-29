import math

def calcular_anos_log(populacao_a, taxa_crescimento_a, populacao_b, taxa_crescimento_b):
    # Calcula o número de anos necessário usando logaritmos
    anos = math.log(populacao_b / populacao_a) / math.log((1 + taxa_crescimento_a) / (1 + taxa_crescimento_b))
    return math.ceil(anos)  # Arredondar para o próximo número inteiro

def main():
    populacao_a = 80000
    taxa_crescimento_a = 0.03  # 3%
    populacao_b = 200000
    taxa_crescimento_b = 0.015  # 1.5%

    anos = calcular_anos_log(populacao_a, taxa_crescimento_a, populacao_b, taxa_crescimento_b)

    print(f"Serão necessários {anos} anos para que a população do país A ultrapasse ou iguale a população do país B.")

if __name__ == "__main__":
    main()
