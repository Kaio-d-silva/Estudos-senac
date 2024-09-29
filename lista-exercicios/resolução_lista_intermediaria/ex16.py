from collections import Counter

def obter_moda(lista):
    contador = Counter(lista)
    moda = contador.most_common(1)
    return moda[0][0] if moda else None

# Exemplo de uso
lista = [4, 2, 2, 8, 3, 3, 3, 4, 4, 4, 7]
moda = obter_moda(lista)

print(f"A moda da lista é: {moda}")
