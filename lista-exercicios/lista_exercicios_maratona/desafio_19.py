def recebe_numero():
    numero_lido = float(input("Informe um numero : "))
    if numero_lido != 0:
        numeros.append(numero_lido)
    else:
        return "sair"

def calcula(lista_numeros):
    soma_total = 0
    for v in lista_numeros:
        soma_total = soma_total + v
    return soma_total

numeros =[]
saida = ""

print(f"\n" + 20 * "-")
print("Para encerrar digite 0")
print(20 * "-")

while saida != "sair":  
    saida = recebe_numero()


total = calcula(numeros)
media = total / len(numeros)

print(f"\n" + 20 * "-")
print(f"A quantidade de numeros digitados é {len(numeros)}, a soma deles é {total}, e sua media é {media:.2f}")
print(20 * "-")