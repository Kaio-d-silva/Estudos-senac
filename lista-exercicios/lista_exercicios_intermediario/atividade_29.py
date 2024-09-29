quantidade_de_numeros = 10
numeros_pares = []
numeros_impares = []


def recebe_numero(n):
    numero = int(input(f"Informe o {n}° numero : "))
    if numero % 2 == 0:
        numeros_pares.append(numero)
    else:
        numeros_impares.append(numero)
    
for n in range(1,quantidade_de_numeros+1):
    recebe_numero(n)
    
print(20 * "-")        
print(f"Dos valores informado, {len(numeros_impares)} são inpares e {len(numeros_pares)} são pares")
print(20 * "-")
