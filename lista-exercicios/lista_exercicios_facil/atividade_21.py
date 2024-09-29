print(20 * "-")
print("** OPÇÕES **\nF - Feminino\nM - Masculino")
print(20 * "-")

entrada = str(input("Informe o sexo : "))


def verifica_sexo(sexo_informado):
    if sexo_informado == "F" or sexo_informado == "f":
        return "Feminino"
    if sexo_informado == "M" or sexo_informado == "m":
        return "Masculino"
    
    return "Sexo invalido"

 
sexo = verifica_sexo(entrada)

print(20 * "-")
print(f"Entrada : {entrada}\nSexo : {sexo}")
print(20 * "-")