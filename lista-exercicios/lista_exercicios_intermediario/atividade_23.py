numeros = []
quantidade_de_numeros = 5


def recebe_numeros(n):
    numero = float(input(f"Informe o {n}° numero : "))
    numeros.append(numero)


for n in range(1, quantidade_de_numeros+1):
    recebe_numeros(n)
    
maior = max(numeros)
menor = min(numeros)

print(f"O maior numero é {maior}, e o menor é {menor}")