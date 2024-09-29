altura = float(input("Informe a altura : "))

peso_ideal_homem = (72.7*altura) - 58
peso_ideal_mulher = (62.1*altura) - 44.7

print(20 * "-")
print(f"O peso ideal para o uma pessoa de {altura} metros é de :\n{peso_ideal_homem:.2f} kilos para homem \n{peso_ideal_mulher} kilos para mulher ")
print(20 * "-")