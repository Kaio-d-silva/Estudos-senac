def area_triangulo(base, altura):
    return (base * altura) / 2

base = float(input("Digite a base do triângulo: "))
altura = float(input("Digite a altura do triângulo: "))
print(area_triangulo(base, altura))