primeira_nota = float(input("Informe a primeira nota : "))
segunda_nota = float(input("Informe a segunda nota : "))


media = (primeira_nota + segunda_nota) / 2

media_necessaria = 7

if media < media_necessaria:
    status = "Reprovado"
if media >= media_necessaria:
    status = "aprovado"
    if media == 10:
        status = "Aprovado com Distinção"

    
    
    
     
print(f"A media deste aluno é {media}, ele foi {status}")