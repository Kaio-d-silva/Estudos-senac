class Contato:
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email

    def __str__(self):
        return f'Nome: {self.nome}, Telefone: {self.telefone}, E-mail: {self.email}'

class Agenda:
    def __init__(self):
        self.contatos = []

    def adicionar_contato(self, contato):
        self.contatos.append(contato)
        print("Contato adicionado com sucesso!")

    def visualizar_contatos(self):
        if not self.contatos:
            print("Nenhum contato na agenda.")
        else:
            for contato in self.contatos:
                print(contato)

    def buscar_contato(self, nome):
        for contato in self.contatos:
            if contato.nome.lower() == nome.lower():
                return contato
        return None

    def remover_contato(self, nome):
        contato = self.buscar_contato(nome)
        if contato:
            self.contatos.remove(contato)
            print("Contato removido com sucesso!")
        else:
            print("Contato não encontrado.")

def menu():
    agenda = Agenda()
    while True:
        print("\nMenu da Agenda de Contatos")
        print("1. Adicionar Contato")
        print("2. Visualizar Contatos")
        print("3. Buscar Contato")
        print("4. Remover Contato")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Digite o nome do contato: ")
            telefone = input("Digite o telefone do contato: ")
            email = input("Digite o e-mail do contato: ")
            contato = Contato(nome, telefone, email)
            agenda.adicionar_contato(contato)
        elif opcao == '2':
            agenda.visualizar_contatos()
        elif opcao == '3':
            nome = input("Digite o nome do contato que deseja buscar: ")
            contato = agenda.buscar_contato(nome)
            if contato:
                print("Contato encontrado:")
                print(contato)
            else:
                print("Contato não encontrado.")
        elif opcao == '4':
            nome = input("Digite o nome do contato que deseja remover: ")
            agenda.remover_contato(nome)
        elif opcao == '5':
            print("Saindo da agenda. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
