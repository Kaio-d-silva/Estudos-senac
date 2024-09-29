numero = int(input("Informe o numero para saber seus divisores : "))


divisores = []


for n in range(1,numero+1):
    if numero % n == 0:
        divisores.append(n)
        
print(divisores)