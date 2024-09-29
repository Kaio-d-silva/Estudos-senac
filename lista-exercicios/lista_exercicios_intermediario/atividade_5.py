a = float(input("Informe o valor de A : "))
b = float(input(f"Informe o valor de B : "))
c = float(input(f"Informe o valor de C : "))

delta = b**2 - 4 * a * c 

raiz1 = (- b + (delta**(1/2)))/(2*a)
raiz2 = (- b - (delta**(1/2)))/(2*a)

print(f"raiz 1 : {raiz1}\nraiz 2 : {raiz2}")