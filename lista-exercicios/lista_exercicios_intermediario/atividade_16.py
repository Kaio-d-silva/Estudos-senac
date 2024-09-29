numeros = [1,2,3,4,5,6,7,8,1,2,1,3,4,6,2,43,2,6,7,85,2,3,0]

maioria = max(set(numeros), key=numeros.count)

print(maioria)