dias = int(input('Digite a quantidade de dias: '))
horas = int(input('Digite a quantidade de horas: '))
minutos = int(input('Digite a quantidade de minutos: '))
segundos = int(input('Digite a quantidade de segundos: '))

def converte_dia_para_hora(dias):
    return dias * 24
def converte_hora_para_minutos(hora):
    return hora * 60
def converte_minuto_para_segundo(minuto):
    return minuto * 60

segundos_dias = converte_minuto_para_segundo(converte_hora_para_minutos(converte_dia_para_hora(dias)))
segundos_horas = converte_minuto_para_segundo(converte_hora_para_minutos(horas))
segundos_minutos = converte_minuto_para_segundo(minutos)

total_segundos = segundos_dias + segundos_horas + segundos_minutos + segundos

print(f'O total de segundos calculado Ã©: {total_segundos}')