tamanho_download = float(input("Informe o tamanho do download (em MBs): "))
velocidade_internet = float(input("Informe a velocidade da internet (em Mbps): "))

tempo_de_download = tamanho_download / (velocidade_internet/8)

print(tempo_de_download)

tempo_em_minutos = tempo_de_download / 60

print(f"Para baixar um arquivo de {tamanho_download} MB com uma velocidade de {velocidade_internet} Mbps, sera necessario {tempo_em_minutos:.2f} minutos")