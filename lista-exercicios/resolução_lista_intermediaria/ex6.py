def tabuada(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")

n = int(input("Digite um número: "))
tabuada(n)