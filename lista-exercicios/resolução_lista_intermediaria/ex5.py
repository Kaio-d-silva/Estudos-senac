import math

def raizes(a, b, c):
    delta = b**2 - 4*a*c
    if delta < 0:
        return "Não há raízes reais"
    elif delta == 0:
        return -b / (2*a)
    else:
        raiz1 = (-b + math.sqrt(delta)) / (2*a)
        raiz2 = (-b - math.sqrt(delta)) / (2*a)
        return raiz1, raiz2

a = float(input("Digite o coeficiente a: "))
b = float(input("Digite o coeficiente b: "))
c = float(input("Digite o coeficiente c: "))
print(raizes(a, b, c))