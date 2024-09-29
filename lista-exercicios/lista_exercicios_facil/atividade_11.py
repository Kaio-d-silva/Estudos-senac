primeiro_numero = int(input("Informe um numero inteiro : "))
segundo_numero = int(input("Informe outro numero inteiro : "))
numero_real = float(input("Informe um numero real : "))

a = 2 * primeiro_numero  + segundo_numero / 2

b = 3 * primeiro_numero + numero_real

c = numero_real ** 3
print(20 *"-")
print(f"O produto do dobro de {primeiro_numero} com metade de {segundo_numero} é : {a} ")
print(20 *"-")
print(f"A soma do triplo de {primeiro_numero} com o {numero_real} é : {b}")
print(20 *"-")
print(f"{numero_real} elevado ao cubo é : {c}")
print(20 *"-")