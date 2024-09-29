km_percorrido = float(input("Informe a quantidade de km/h percorridos : "))
quantidade_dias = float(input("Informe por quantos dias o carro foi alugado : "))

valor_dia = 60
valor_km_rodado = 0.15

valor_a_pagar = (quantidade_dias * valor_dia) + (km_percorrido * valor_km_rodado)
print("\n" + 20 * "-")
print(f"Valor a pagar {valor_a_pagar:.2f} R$")
print(20 * "-")