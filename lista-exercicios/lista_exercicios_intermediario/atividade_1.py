numero = int(input("Informe um numero : "))

if numero < 100:
    soma = 0
    numero_convertido = list(str(numero))
    for n in numero_convertido:
        soma += int(n)
    print(f"A soma dos digitos de {numero} é {soma}")    

else:
    print("O numero deve ser menor que 100")

  