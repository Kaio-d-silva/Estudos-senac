def validar_nome():
    while True:
        nome = input("Digite seu nome (maior que 3 caracteres): ")
        if len(nome) > 3:
            return nome
        else:
            print("Erro: O nome deve ter mais de 3 caracteres.")


def validar_idade():
    while True:
        try:
            idade = int(input("Digite sua idade (entre 0 e 150): "))
            if 0 <= idade <= 150:
                return idade
            else:
                print("Erro: A idade deve ser entre 0 e 150.")
        except ValueError:
            print("Erro: Por favor, insira um número inteiro válido.")


def validar_salario():
    while True:
        try:
            salario = float(input("Digite seu salário (maior que zero): "))
            if salario > 0:
                return salario
            else:
                print("Erro: O salário deve ser maior que zero.")
        except ValueError:
            print("Erro: Por favor, insira um valor numérico válido.")


def validar_sexo():
    while True:
        sexo = input(
            "Digite seu sexo ('f' para feminino, 'm' para masculino): ").lower()
        if sexo in ['f', 'm']:
            return sexo
        else:
            print("Erro: O sexo deve ser 'f' ou 'm'.")


def validar_estado_civil():
    while True:
        estado_civil = input(
            "Digite seu estado civil ('s' para solteiro(a), 'c' para casado(a), 'v' para viúvo(a), 'd' para divorciado(a)): ").lower()
        if estado_civil in ['s', 'c', 'v', 'd']:
            return estado_civil
        else:
            print("Erro: O estado civil deve ser 's', 'c', 'v' ou 'd'.")


def main():
    nome = validar_nome()
    idade = validar_idade()
    salario = validar_salario()
    sexo = validar_sexo()
    estado_civil = validar_estado_civil()

    print("\nInformações validadas:")
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print(f"Salário: R$ {salario:.2f}")
    print(f"Sexo: {'Feminino' if sexo == 'f' else 'Masculino'}")
    print(f"Estado Civil: {estado_civil.upper()}")


if __name__ == "__main__":
    main()