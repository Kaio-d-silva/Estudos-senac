def intercalar(lista1, lista2):
    resultado = []
    while lista1 and lista2:
        if lista1[0] < lista2[0]:
            resultado.append(lista1.pop(0))
        else:
            resultado.append(lista2.pop(0))
    resultado.extend(lista1)
    resultado.extend(lista2)
    return resultado

lista1 = [1, 3, 5]
lista2 = [2, 4, 6]
print(intercalar(lista1, lista2))