import os


def verifica_abertura(modo_abertura,arquivo_selecionado):
    f = open(arquivo_selecionado, "r")
    if modo_abertura == 'l':
        #Somente leitura do arquivo
        print(f'\n{f.read()}\n')
        
    elif modo_abertura == "a":
        #leitura e alteracao do arquivo
        print(f'\n{f.read()}\n')
        mensagem = input('Oque sera escrito no texto :\n')
        mensagem_formatada = f'\n{mensagem}'
        
        with open(arquivo_selecionado,'a') as arquivo:
            arquivo.write(mensagem_formatada)
            arquivo.close()
            f = open(arquivo_selecionado, "r")
            print(f'\n{f.read()}\n')
            
    elif modo_abertura == "i":
        print("\n")
        os.system(f"python3 {arquivo_selecionado}")
        
    else:
        print('Modo de abertura não disponivel.')
