print(20 * "-")
print("** OPÇÕES **\nM - Matutino\nV - Vespertino\nN - Noturno")
print(20 * "-")

entrada = str(input("Informe o turno : "))


def verifica_turno(turno_informado):
    if turno_informado == "M" or turno_informado == "m":
        return "Matutino"
    if turno_informado == "N" or turno_informado == "n":
        return "Noturno"
    if turno_informado == "V" or turno_informado == "v":
        return "Vespertino"
    
    return "Turno invalido"

 
turno = verifica_turno(entrada)

print(20 * "-")
print(f"Entrada : {entrada}\nTurno : {turno}")
print(20 * "-")