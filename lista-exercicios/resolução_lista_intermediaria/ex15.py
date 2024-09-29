def devolver_mes():
    data = input("Digite a data no formato DDMMAAAA: ")
    mes = data[2:4]
    meses = {
        "01": "Janeiro",
        "02": "Fevereiro",
        "03": "Março",
        "04": "Abril",
        "05": "Maio",
        "06": "Junho",
        "07": "Julho",
        "08": "Agosto",
        "09": "Setembro",
        "10": "Outubro",
        "11": "Novembro",
        "12": "Dezembro"
    }
    print(f"Mês: {meses[mes]}")

devolver_mes()