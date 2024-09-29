numeros = []

limite_numeros = 10

index = 0

def recebe_numero(index):
    numero_recebido = int(input(f"Informe um numero, este é o {index+1}° numero : "))
    numeros.append(numero_recebido)
    index += 1
    return index
    


while index != limite_numeros:
    index = recebe_numero(index)
    
menor_numero = min(numeros)
maior_numero = max(numeros) 
soma = menor_numero + maior_numero 

print(20 * "-")
print(f"A soma de {menor_numero} (menor dos numeros) e {maior_numero} (maior dos numeros) é {soma}")
print(20 * "-")