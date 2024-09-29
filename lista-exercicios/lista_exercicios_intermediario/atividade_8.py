palavra = str(input("Informe uma palavra : "))

palavra = list(palavra)
palavra_invertida = list(palavra)
palavra_invertida.reverse()

if palavra == palavra_invertida:
    texto = "é uma palindrome"
else:
    texto = "não é uma palindrome"
    
print(20 * "-")
print(f"Esta palavra {texto}")
print(20 * "-")



