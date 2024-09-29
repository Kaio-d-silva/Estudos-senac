deposito_inicial = float(input("Informe o deposito inicial : "))
taxa_de_juros = float(input("Informe a taxa de juros : "))

saldo = deposito_inicial 
meses = 24
  
for m in range(meses):
    saldo += + (saldo * (taxa_de_juros/100))
    print(f"Mes {m}, Saldo : {saldo:.2f}")