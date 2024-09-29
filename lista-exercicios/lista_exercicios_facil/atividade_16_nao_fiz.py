metros_quadrados = float(input("Informe a quantidade de metros quadrados da area a ser pintada : "))

litros_necessarios = metros_quadrados / 3
# litros 1/3


tamanho_lata_grande = 18
valor_lata_grande = 80

tamanho_lata_pequena = 3.6
valor_lata_pequena = 25

def quantidade_de_latas(quantidade_de_litros): 
    quanto_comprar = litros_necessarios / quantidade_de_litros
    quanto_comprar_inteiro = int(quanto_comprar)
    teste = quanto_comprar % quanto_comprar_inteiro
    print(teste)
    
    if quanto_comprar % quanto_comprar_inteiro != 0 :
        quanto_comprar = + 1
    return quanto_comprar_inteiro
        
def valor_tinta(valor_por_lata,quantidade_de_latas):
    valor_total = quantidade_de_latas * valor_por_lata
    return valor_total

# sobra_de_tinta = (tinta_a_ser_usada / tamanho_lata) - quanto_comprar



print(f"Em {metros_quadrados} metros, serão usadaos {litros_necessarios:.2f} litros de tinta")

quantidade_de_grande = quantidade_de_latas(tamanho_lata_grande)
total_lata_grande = valor_tinta(valor_lata_grande,quantidade_de_grande)
print(f"Comprando apenas latas de 18 litros, o valor gasto sera de {total_lata_grande} ")

quantidade_de_pequena = quantidade_de_latas(tamanho_lata_grande)
total_lata_pequena = valor_tinta(valor_lata_pequena,quantidade_de_pequena)
print(f"Comprando apenas latas de 3.6 litros, o valor gasto sera de {total_lata_pequena} ")