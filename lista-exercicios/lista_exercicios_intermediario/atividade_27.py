primeiro_numero = int(input("Informe um numero : "))
segundo_numero = int(input("Informe outro numero : "))

numeros = [primeiro_numero, segundo_numero]
soma = 0

for n in range(min(numeros)+1, max(numeros)):
    soma += n 
    print(n)
    
print(f"Os numeros no intervalo {primeiro_numero} ao {segundo_numero} tem como soma {soma} ")    
    