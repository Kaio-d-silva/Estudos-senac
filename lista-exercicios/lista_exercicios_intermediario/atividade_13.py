maximo_de_numeros = 10
index = 0
numeros = []
soma = 0

def recebe_numero():
    global soma
    numero_recebido = int(input("Informe um numero : "))
    numeros.append(numero_recebido)
    soma += numero_recebido



while index < maximo_de_numeros:
    recebe_numero()
    index += 1

media = soma/maximo_de_numeros

print(f"A soma dos {maximo_de_numeros} numeros é {soma}, e sua media é de {media}")
