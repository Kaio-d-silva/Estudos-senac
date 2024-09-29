def imprimir_segunda_linha(lista_de_listas):
    if len(lista_de_listas) >= 2:
        print("Segunda linha completa:")
        print(lista_de_listas[1])
    else:
        print("A lista de listas não contém uma segunda linha.")

# Programa principal
lista_de_listas = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

imprimir_segunda_linha(lista_de_listas)
