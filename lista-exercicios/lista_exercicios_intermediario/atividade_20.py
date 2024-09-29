populacao_a = 80000
taxa_crecimento_a = 3/100

populacao_b = 200000
taxa_crecimento_b = 1.5/100

populacao_total_a = populacao_a
populacao_total_b = populacao_b

quantidade_anos = 0

while populacao_total_a <= populacao_total_b:
    populacao_total_a +=  populacao_total_a * taxa_crecimento_a 
    populacao_total_b +=  populacao_total_b * taxa_crecimento_b 
    quantidade_anos += 1

print(f"Serão necessários {quantidade_anos} anos para que a população do país A ultrapasse ou iguale a população do país B.")