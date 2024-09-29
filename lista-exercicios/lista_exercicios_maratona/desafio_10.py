# 10. Escreva um programa que calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média esperada para a viagem.

distancia = float(input("Informe a distancia a ser percorrida : "))
velocidade = float(input("Informe a velocidade media : "))

tempo_de_viagem = distancia / velocidade

horas = int(tempo_de_viagem)

minutos = int((tempo_de_viagem - horas) * 60)

print(f"Para percorrer {distancia}km, a uma velociade de {velocidade}km/h voce vai levar {horas} horas, {minutos} minnutos")


