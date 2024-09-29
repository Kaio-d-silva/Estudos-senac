import time 

inicio = time.time()


numeros = [1,1]
parada = 50

def sequencia_de_fibonati(anterior,corrente, parada):
    if parada == 0:
       return 
    novo_corrente = anterior + corrente
    numeros.append(novo_corrente)
    parada -= 1
    sequencia_de_fibonati(corrente,novo_corrente,parada)
       

sequencia_de_fibonati(1,1, parada)
print(50 * "-")
print(numeros)
print(50 * "-")

termino = time.time()

tempo_de_execucao = termino - inicio

# print(f"inicio : {inicio}\nfim : {termino}\nresultado : {fim} segundos")
print(f"resultado : {tempo_de_execucao} segundos\n")