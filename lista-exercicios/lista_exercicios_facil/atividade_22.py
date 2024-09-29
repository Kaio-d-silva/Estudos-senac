print(20 * "-")
letra_informado = str(input("Informe uma letra : "))

vogais = ["a","e","i","o","u"]

status = "consoante"

if letra_informado in vogais:
    status = "Vogal"
    
print(20 * "-")
print(f"A letra {letra_informado} é uma {status}")