def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        # Para cada passagem pelo array, o maior elemento "flutua" para o final
        for j in range(0, n-i-1):
            # Troca se o elemento atual for maior que o próximo
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]

# Programa principal
try:
    # Entrada do usuário para a lista de números
    lista = []
    quantidade = int(input("Quantos números você deseja ordenar? "))
    
    for i in range(quantidade):
        numero = int(input(f"Digite o {i+1}º número: "))
        lista.append(numero)
    
    print(f"\nLista antes da ordenação: {lista}")
    bubble_sort(lista)
    print(f"Lista após a ordenação (Bubble Sort): {lista}")

except ValueError:
    print("Por favor, insira um número inteiro válido.")
