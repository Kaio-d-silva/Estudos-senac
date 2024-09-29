valor_mercadoria = float(input("Informe o valor da mercadoria: ")) 
valor_desconto = float(input("Informe o percentual de desconto: "))

total_descontado = valor_mercadoria * (valor_desconto/100 )
valor_a_pagar = valor_mercadoria - total_descontado

print("\n" + 20 * "-")
print(f"Valor de desconto {total_descontado:.2f}R$\nValor a pagar {valor_a_pagar:.2f}R$") 
print(20 * "-")