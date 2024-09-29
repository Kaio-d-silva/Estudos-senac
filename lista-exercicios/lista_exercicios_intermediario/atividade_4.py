numero = int(input("Informe um numero : "))


status = "Impar"

if numero % 2 == 0:
    status = "Par"
    
print(f"O numero {numero} é {status}")