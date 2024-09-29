primeiro_numero =  float(input("Escreva um numero : "))
segundo_numero = float(input("Escreva outro numero : "))
terceiro_numero = float(input("Escreva mais um numero : "))

numeros = [primeiro_numero, segundo_numero, terceiro_numero]

numeros_ordenados = sorted(numeros)


print(f"Numeros ordenados : {numeros_ordenados[0]}, {numeros_ordenados[1]}, {numeros_ordenados[2]}")
