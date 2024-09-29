numeros = []
quantidade_de_numeros = 5
soma = 0

def recebe_numeros(n):
    global soma
    numero = float(input(f"Informe o {n}° numero : "))
    numeros.append(numero)
    soma += numero


for n in range(1, quantidade_de_numeros+1):
    recebe_numeros(n)
    
    

media = soma/len(numeros)

print(f"A soma dos nuneros é {soma} e a media é {media}")