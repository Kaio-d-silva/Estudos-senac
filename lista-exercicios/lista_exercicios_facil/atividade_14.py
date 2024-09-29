peso = float(input("Informe o peso dos peixes : "))

peso_maximo = 50
multa_por_kilo = 4
exesso = peso - peso_maximo

if peso > peso_maximo:
    multa = exesso * multa_por_kilo 

print(f"Você teve um exesso de {exesso} kilos, o valor da multa é {multa:.2f}")
