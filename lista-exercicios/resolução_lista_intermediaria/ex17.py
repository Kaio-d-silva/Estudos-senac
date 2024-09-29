def pedir_nota():
    while True:
        try:
            nota = float(input("Digite uma nota entre 0 e 10: "))
            if 0 <= nota <= 10:
                return nota
            else:
                print("Nota inválida. Por favor, digite um valor entre 0 e 10.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

# Exemplo de uso
nota_valida = pedir_nota()
print(f"Você digitou a nota: {nota_valida}")
