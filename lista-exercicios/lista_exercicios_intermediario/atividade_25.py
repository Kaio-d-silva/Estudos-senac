# Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50. 

quantidade_de_numeros = 50

for n in range(0, quantidade_de_numeros):
    if n % 2 != 0:
        print(f"numero : {n}")