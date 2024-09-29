primeiro_numero = float(input("Digite o primeiro numero : "))
segundo_numero = float(input("Digite o segundo numero : "))
print("\n" + 20 * "-")
print("** Operações permitidas **\nAdioção : +\nSubtração : -\nMultiplicação : *\nDivisão : /")  
print(20 * "-")

operacao = str(input("informe a operacao : "))

def calcula(valor1, operador, valor2):
    if operador == "+":
        return valor1 + valor2
    if operador == "-":
        return valor1 - valor2
    if operador == "*":
        return valor1 * valor2
    if operador == "/":
        return valor1 / valor2
    
 
    
resultado = calcula(primeiro_numero, operacao, segundo_numero)
print(f"O resultado de {primeiro_numero} {operacao} {segundo_numero} é {resultado}")