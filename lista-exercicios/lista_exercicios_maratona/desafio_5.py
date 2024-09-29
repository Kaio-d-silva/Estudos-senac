a = int(input("Escolha um valor: "))
b = int(input("Escolha outro valor : "))


def calcula(valor1, valor2):
    resultado = valor1 + valor2
    print(f"O resultado da soma de {valor1} + {valor2} é {resultado}")
    
calcula(a,b)