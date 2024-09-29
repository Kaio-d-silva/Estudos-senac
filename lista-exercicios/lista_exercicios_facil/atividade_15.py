valor_hora = float(input("Informe o valor da sua hora : "))
quantidade_horas = float(input("Informe a quantidade de horas trabalhadas no mes : "))

salario_bruto = valor_hora * quantidade_horas
ir = salario_bruto * 11/100
inss = salario_bruto * 8/100
sindicado = salario_bruto * 5/100

descontos = ir + inss + sindicado

salario_liquido = salario_bruto - descontos

# a. quanto pagou ao INSS.
# b. quanto pagou ao sindicato.
# c. o salário líquido.
# d. calcule os descontos e o salário líquido
print(20 * "-")
print(f" **Detalhando salario**\n")
print(f"Salario bruto : {salario_bruto:.2f}\nIR : {ir:.2f}\nINSS : {inss:.2f}\nSindicato : {sindicado:.2f}\nSalario Liquido : {salario_liquido:.2f}")
print(20 * "-")