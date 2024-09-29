valor_a_pagar = 0
saida = ""
compras = []

valores_produtos = {
    1 : 0.50,
    2 : 1.00,
    3 : 4.00,
    5 : 7.00,
    9 : 8.00  
}
  
def itens_comprados():
    print("\n" + 40 * "-")
    codigo_produto = int(input("Informe o codigo do produto (ou 0 para sair): "))
    if codigo_produto != 0:
        if codigo_produto in valores_produtos:
            print(40 * "-")
            quantidade_comprada = int(input("Informe a quantidade de produtos comprados : "))
            valor = calcula_valor(codigo_produto,quantidade_comprada)
            global valor_a_pagar
            valor_a_pagar += valor
            compras.append({"codigo": codigo_produto, "quantidade" : quantidade_comprada, "valor" : valor})
            #print(compras)
        else:
            print("codigo invalido")
    else:
        return "sair"


def calcula_valor(codigo, quantidade):
    valor = valores_produtos[codigo] * quantidade
    return valor

  
while saida != "sair":  
    saida = itens_comprados()
    
print(f"Total de compras : {valor_a_pagar:.2f} R$")

