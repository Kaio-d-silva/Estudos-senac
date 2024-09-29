primeiro_preco =  float(input("Escreva o valor de um produto em reais : "))
segundo_preco = float(input("Escreva outro valor em reais : "))
terceiro_preco = float(input("Escreva mais um valor em reais : "))

precos = [primeiro_preco, segundo_preco, terceiro_preco]

maior_preco = max(precos)
menor_preco = min(precos)
print(20 * "-")
print(f"O maior valor é {maior_preco}R$, o e menor é {menor_preco}R$")
print(20 * "-")
print(f"Recomendo comprar o produto de valor {menor_preco}R$")
print(20 * "-")