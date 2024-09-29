def calcular_potencia(base, expoente):
    resultado = 1
    for _ in range(abs(expoente)):
        resultado *= base
    
    # Se o expoente for negativo, invertemos o resultado
    if expoente < 0:
        resultado = 1 / resultado
    
    return resultado

# Programa principal
try:
    base = float(input("Digite o número base: "))
    expoente = int(input("Digite o número expoente: "))
    resultado = calcular_potencia(base, expoente)
    print(f"{base} elevado a {expoente} é igual a {resultado}")
except ValueError:
    print("Por favor, insira valores numéricos válidos.")
