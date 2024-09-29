class Pessoa:
    def __init__(self, nome:str) -> None:
        self.nome = nome
        
    def mostra_nome(self):
        print(f"O nome é {self.nome}")
        

class Professor(Pessoa):
    def __init__(self, nome, titulacao) -> None:
        super().__init__(nome)
        self.titulacao = titulacao
        
    def mostra_titulacao(self):
        print(f"Sua titulação é {self.titulacao}")    



pessoa1 = Pessoa("kaio")
pessoa1.mostra_nome()

professor1 = Professor("jorge", "Matematica")
professor1.mostra_nome()
professor1.mostra_titulacao()