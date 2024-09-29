nome = str(input("Informe o Nome : "))
idade = int(input("Informe a Idade : "))
salario = float(input("Infome o salario : "))
sexo = str(input("Informe o Sexo : "))
estado_civil = str(input("Informe o Estado civil : "))

def validar(item, valor):
    if item == "nome":
        status = valida_nome(valor)
        return status
    elif item == "idade":
        status = valida_idade(valor)
        return status
    elif item == "salario":
        status = valida_salario(valor)
        return status
    elif item == "sexo":
        status = valida_sexo(valor)
        return status
    elif item == "estado_civil":
        status = valida_estado_civil(valor)
        return status

    



def valida_nome(nome):
    return "Invalido" if len(nome) < 3 else "Valido"
    
def valida_idade(idade):
    return "Invalido" if idade == range(0,150) else "Valido"

def valida_salario(salario):
    return "Invalido" if salario < 0 else "Valido"

def valida_sexo(sexo):
    respostas_sexo = ["f", "F", "m", "M"]
    return "Invalido" if sexo not in respostas_sexo else "Valido"

def valida_estado_civil(estado_civil):
    respostas_estado_civil = ["s", "S", "c", "C", "v", "V", "d", "D"]
    return "Invalido" if estado_civil not in respostas_estado_civil else "Valido" 
     
    

status_nome = validar("nome", nome)
status_idade = validar("idade", idade)
status_salario = validar("salario", salario)
status_sexo = validar("sexo", sexo)
status_estado_civil= validar("estado_civil", estado_civil)








print(f"{nome} : {status_nome} ")
print(f"{idade} : {status_idade} ")
print(f"{salario} : {status_salario} ")
print(f"{sexo} : {status_sexo} ")
print(f"{estado_civil} : {status_estado_civil} ")