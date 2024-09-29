# original_numeros = [14, 3, 18, 7, 1, 19, 13, 9, 4, 17, 20, 5, 8, 15, 6, 2, 12, 10, 11, 16]

# numeros = original_numeros.copy()

# print('start')
# # Repete o processo pela quantidade de itens
# for item in numeros:
    
#     # Passa por valor da lista 
#     for numero in numeros:
        
#         # Pega a posição do proximo numero 
#         posicao_prox_numero = (numeros.index(numero))+1
        
#         # Verifica se a posição existe na lista
#         if posicao_prox_numero < len(numeros):
            
#             # Verifica se o valor é maior que o valor da proxima posição 
#             if numero > numeros[posicao_prox_numero]:
#                 #print(numeros[posicao_prox_numero])
#                 # Remove item maior da lista
#                 numeros.remove(numero)
                
#                 # Adiciona item na posição correta (posterior ao menor)
#                 numeros.insert(posicao_prox_numero, numero)
            
          
# print(f"lista original : {original_numeros}\nLista ordenada : {numeros}")


original_numeros = [14, 3, 18, 7, 1, 19, 13, 9, 4, 17, 20, 5, 8, 15, 6, 2, 12, 10, 11, 16]

numeros = original_numeros.copy()

print('start')

# Implementação do Bubble Sort
for i in range(len(numeros)):
    for j in range(len(numeros) - 1 - i):
        if numeros[j] > numeros[j + 1]:
            # Troca os elementos se estiverem na ordem errada
            numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]

print(f"lista original : {original_numeros}\nLista ordenada : {numeros}")

