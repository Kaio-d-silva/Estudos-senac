def recebe_nota():
    nota = float(input("Informe uma nota de 0 a 10 : "))
         
    if nota > 10 or nota < 0:
        print("Valor invalido")
    else:
        return "sair"
    
    
saida = ""

while saida != "sair":
    saida = recebe_nota()
    