valor_salario = float(input("Digite o valor do salario : "))
percentual = float(input("digite o percentual do aumento: "))

def calcula_aumento(salario, percentual):
    porcentagem = percentual / 100
    print(percentual)
    aumento = salario * porcentagem
    salario_final = salario + (salario * porcentagem) 
    print(f" O aumento foi de {aumento}, e o salario final é {salario_final}")
    
    
calcula_aumento(valor_salario, percentual)