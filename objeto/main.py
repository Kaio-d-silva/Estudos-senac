class Aluno:
    # Atributos - propriedades, dados da classe - objeto
    def __init__(self):
        # self.idade = idade
        # self.nome = nome
        self.lista_alunos = [{"Nome" : "Kaio", "idade" : 19, "matricula" : 1}]
        self.matricula = 0 
        
    # Metodos - funcoes, como manipular o objeto
    
    def adiciona_aluno(self, nome, idade):
        self.lista_alunos.append(f"Nome :{nome} idade: {idade} matricula: {self.matricula + 1}")
        self.matricula = self.matricula + 1
        



funcao = int(input("Consulta aluno - 1\nCadastro Aluno - 2\n"))

if funcao == 2:
   nome = input("Nome do aluno: ")
   idade = int(input("Idade do aluno: ")) 
   novo_aluno = Aluno()
   novo_aluno.adiciona_aluno(nome, idade)
   print(novo_aluno.lista_alunos)
   
elif funcao == 1:
    matricula = input ("Numero da matricula : ")
    aluno_consulta = Aluno()

    index = -1
    for aluno in aluno_consulta.lista_alunos:
        index + 1 
        for campo in aluno:
            if campo == "matricula":
                resultado = aluno_consulta.lista_alunos[index]
                print(resultado)
                
