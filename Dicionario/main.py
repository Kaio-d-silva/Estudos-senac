lista_aluno = [{"nome":"kaio","idade":19},{"nome":"carlos","idade":20}]

def criar_pessoa(nome, idade):
    pessoa = {} 
    pessoa["nome"] = nome
    pessoa["idade"]= idade
    return pessoa

tamanho_lista = len(lista_aluno)
index = 0

while(tamanho_lista> 0):
    pessoa = criar_pessoa(lista_aluno[index]["nome"],lista_aluno[index]["idade"])
    print(pessoa)

    tamanho_lista = tamanho_lista - 1
    index = index + 1
