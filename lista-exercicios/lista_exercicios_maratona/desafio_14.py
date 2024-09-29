salario = float(input("Informe seu salario : "))

valor_separador = 1250 

aumento = 15 # percentual do aumento

if salario > valor_separador:
    salario_final = salario + (salario * 0.10)
    aumento = 10
else:
    salario_final = salario = (salario * 0.15)
    

print("\n" + 20 * "-")
print(f"O seu novo salario é {salario_final:.2f}R$\naumento de {aumento}%")
print(20 * "-")