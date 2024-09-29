
lista_1 = [1,2,3,4,5,6,7,8,9] 
lista_2 = ["a","b","c","d","e"]


lista_intercalada = []

for l1, l2 in zip(lista_1,lista_2):
    lista_intercalada.append(l1)
    lista_intercalada.append(l2)
    
print(lista_intercalada)
    