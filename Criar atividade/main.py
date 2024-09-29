from pathlib import Path
import os
from sys import exit

# Buscar diretório
diretorio_home = Path.home()

# Navegar até diretorio
os.chdir(diretorio_home)

# Cria diretório se ele não existir
diretorio_projetos = f'{diretorio_home}/Projetos'
if os.path.exists(diretorio_projetos) == False:
    os.mkdir(diretorio_projetos)
    
# Navegar até diretório 
os.chdir(diretorio_projetos)

# Recebe nome da atividade e verifica se ela ja existe
saida = 0
while saida != 1:
    atividade = input("Qual a atividade: ")
    diretorio_final = f'{diretorio_projetos}/{atividade}'
    if atividade == 'exit' or 'sair':
        exit("Saindo...")
    elif os.path.exists(diretorio_final) == False:
        os.mkdir(atividade)
        os.chdir(diretorio_final)
        os.mknod('main.py')
        print(diretorio_final)
        print(os.listdir(diretorio_final))
        saida = 1
    else:
        print('\nDiretório ja existe, escreva outro:\n')
        
