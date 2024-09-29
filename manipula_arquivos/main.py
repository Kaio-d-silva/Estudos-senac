import os
from listar_diretorio import listar
from valores_recebidos import recebe_caminho, recebe_modo_abertura 


caminho_arquivo = recebe_caminho('escoha o diretorio do arquivo : ')
listar(caminho_arquivo)



if os.path.exists(caminho_arquivo):
    
    modo_abertura = recebe_modo_abertura()
    caminho_arquivo = recebe_caminho('\nqual arquivo deseja abrir : ')
    f = open(caminho_arquivo, "r")
    
    if modo_abertura == 'l':
        #Somente leitura do arquivo
        print(f'\n{f.read()}\n')

    elif modo_abertura == "a":
        #leitura e alteracao do arquivo
        print(f'\n{f.read()}\n')

        mensagem = input('Oque sera escrito no texto :\n')
        mensagem_formatada = f'\n{mensagem}'

        with open(caminho_arquivo,'a') as arquivo:
            arquivo.write(mensagem_formatada)
            arquivo.close()
            f = open(caminho_arquivo, "r")
            print(f'\n{f.read()}\n')

    else:
        print('Modo de abertura não disponivel.')
else: 
    print(f"o Caminho {caminho_arquivo} é inexistente.")