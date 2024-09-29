matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

soma_total = 0

for linha in matriz:
    for valor in linha:
        soma_total += valor
        
print(f"A soma de todos os elementos da matriz é {soma_total}")