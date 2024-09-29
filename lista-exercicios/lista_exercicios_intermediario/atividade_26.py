# Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles. 

primeiro_numero = int(input("Informe um numero : "))
segundo_numero = int(input("Informe outro numero : "))

numeros = [primeiro_numero, segundo_numero]

for n in range(min(numeros)+1, max(numeros)):
    print(n)