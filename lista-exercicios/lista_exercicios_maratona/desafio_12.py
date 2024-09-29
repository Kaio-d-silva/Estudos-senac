# 12. Escreva um programa que pergunte a velocidade do carro de um usuário. Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário foi multado. Nesse caso, exiba o valor da multa, cobrando R$ 5 por km acima de 80 km/h.

velocidade_carro = float(input("Informe a velocidade do carro : "))

velocidade_maxima = 80
multa_por_km = 5

if velocidade_carro > velocidade_maxima:
    valor_multa = multa_por_km * (velocidade_carro - velocidade_maxima) 
    
    print("\n" + 20 * "-")
    print(f"Você foi multado !!!\nValor da multa {valor_multa:.2f}R$")
    print(20 * "-")
