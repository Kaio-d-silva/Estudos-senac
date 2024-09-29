populacao_a = int(input("Informe a primeira população : "))
taxa_crecimento_a = float(input("Informe a taxa de crecimento : "))

populacao_b = int(input("Informe a segunda população : "))
taxa_crecimento_b = float(input("Informe a taxa de crecimento : "))

populacao_total_a = populacao_a
populacao_total_b = populacao_b

quantidade_anos = 0

teste = 0

while populacao_total_a <= populacao_total_b:
    populacao_total_a +=  (populacao_total_a * (taxa_crecimento_a/100)) 
    populacao_total_b +=  (populacao_total_b * (taxa_crecimento_b/100)) 
    quantidade_anos += 1


print(f"Serão necessários {quantidade_anos} anos para que a população do país A ultrapasse ou iguale a população do país B.")