# Definição da classe Pessoa
class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def apresentar(self):
        return f"Nome: {self.nome}"

# Definição da classe Professor, que herda de Pessoa
class Professor(Pessoa):
    def __init__(self, nome, titulacao):
        super().__init__(nome)  # Chama o construtor da classe base (Pessoa)
        self.titulacao = titulacao

    def apresentar(self):
        return f"Nome: {self.nome}, Titulação: {self.titulacao}"

# Programa principal
def main():
    pessoa = Pessoa("João")
    print(pessoa.apresentar())

    professor = Professor("Maria", "Doutora")
    print(professor.apresentar())

if __name__ == "__main__":
    main()
