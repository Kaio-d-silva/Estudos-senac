primeiro_numero =  float(input("Escreva um numero : "))
segundo_numero = float(input("Escreva outro numero : "))
terceiro_numero = float(input("Escreva mais um numero : "))

numeros = [primeiro_numero, segundo_numero, terceiro_numero]

maior_numero = max(numeros)

print(f"O maior numero é {maior_numero}")