numero = float(input("Informe um numero : "))

status = "Positivo"

if numero < 0:
    status = "Negativo"
    
print(f"O numero {numero} é {status} ")