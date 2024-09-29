valor_casa = float(input("Informe o valor da casa em R$: "))
salario = float(input("Informe o seu salario : "))
quantidade_anos = float(input("Informe a quantidade de anos para pagar: "))

quantidade_meses = quantidade_anos * 12
prestacao_mensal = valor_casa / quantidade_meses

if prestacao_mensal > (salario * 0.30):
    valor_necessario = salario * 0.30
    print(f"Emprestimo negado, o valor de {prestacao_mensal:.2f}R$ é maior que o permitido\n Valor necessario para permitir {valor_necessario:.2f}R$")
else:
    print(20 * "-")
    print("Emprestimo aprovado !!!") 
    print(20 * "-")