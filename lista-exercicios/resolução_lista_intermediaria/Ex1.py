def soma_digitos(n):
    return sum(int(d) for d in str(n))

n = int(input("Digite um número menor que 100: "))
print(soma_digitos(n))
