lista_aluno = [{"nome":"kaio","idade":19},{"nome":"carlos","idade":20}]

class Pessoa:
    def __init__(self):
        ...
        
    def self_idade(self, idade):
        self.idade = idade
    
    def self_nome(self, nome):
        self.nome = nome
        
        

tamanho_lista = len(lista_aluno)
index = 0
while(tamanho_lista> 0):
    pessoa = Pessoa()
    pessoa.self_nome(lista_aluno[index]["nome"])
    pessoa.self_idade(lista_aluno[index]["idade"])
    print(pessoa.idade)
    print(pessoa.nome)

    tamanho_lista = tamanho_lista - 1
    index = index + 1
    
