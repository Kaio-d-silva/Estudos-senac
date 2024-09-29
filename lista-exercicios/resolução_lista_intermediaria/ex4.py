def par_ou_impar(n):
    if n % 2 == 0:
        return "Par"
    else:
        return "Ímpar"

n = int(input("Digite um número: "))
print(par_ou_impar(n))