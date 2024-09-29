import math

# Função para calcular a quantidade de tinta necessária
def calcular_tinta( area ):
    cobertura_por_litro = 3
    folga = 1.1
    litros_necessarios = (area / cobertura_por_litro) * folga
    return litros_necessarios

# Função para calcular a quantidade de latas e galões
def calcular_latas_e_galoes( litros_necessarios ):
    litros_lata = 18
    litros_galao = 3.6

    # Cálculo para apenas latas
    latas = math.ceil(litros_necessarios / litros_lata)
    custo_latas = latas * 80

    # Cálculo para apenas galões
    galoes = math.ceil(litros_necessarios / litros_galao)
    custo_galoes = galoes * 25

    # Cálculo para combinação de latas e galões
    latas_mistura = math.floor(litros_necessarios / litros_lata)
    litros_restantes = litros_necessarios - (latas_mistura * litros_lata)
    galoes_mistura = math.ceil(litros_restantes / litros_galao)
    custo_mistura = (latas_mistura * 80) + (galoes_mistura * 25)

    return latas, custo_latas, galoes, custo_galoes, latas_mistura, galoes_mistura, custo_mistura

# Função principal do programa
def main():
    # Entrada do usuário
    area = float(input("Digite o tamanho da área a ser pintada em metros quadrados: "))

    # Calcular a quantidade de tinta necessária
    litros_necessarios = calcular_tinta(area)
    print(f"Litros de tinta necessários (com folga de 10%): {litros_necessarios:.2f} litros")

    # Calcular quantidades e custos
    latas, custo_latas, galoes, custo_galoes, latas_mistura, galoes_mistura, custo_mistura = calcular_latas_e_galoes(litros_necessarios)

    # Exibir os resultados
    print("\nOpções de compra:")
    print(f"1. Comprar apenas latas de 18 litros:")
    print(f"   - Quantidade de latas: {latas} lata(s)")
    print(f"   - Custo total: R$ {custo_latas:.2f}")

    print(f"2. Comprar apenas galões de 3,6 litros:")
    print(f"   - Quantidade de galões: {galoes} galão(ões)")
    print(f"   - Custo total: R$ {custo_galoes:.2f}")

    print(f"3. Misturar latas e galões:")
    print(f"   - Quantidade de latas: {latas_mistura} lata(s)")
    print(f"   - Quantidade de galões: {galoes_mistura} galão(ões)")
    print(f"   - Custo total: R$ {custo_mistura:.2f}")

# Executar o programa
if __name__ == "__main__":
    main()
