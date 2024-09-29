from os import listdir

def listar(path):
    print(f'\nArquivos no diretorio :')
    for c in listdir(path):
        print(c)
    print('\n')