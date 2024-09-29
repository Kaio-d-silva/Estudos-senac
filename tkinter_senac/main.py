from tkinter import Label, Button, Text, Tk, Frame, RIGHT, YES, X

# def cria_frame(nome_frame, cor):
#     nome_frame = Frame(root, width=600, highlightbackground=cor, highlightcolor=cor, highlightthickness=5, height=200)
#     return nome_frame




root = Tk()
root.title("Criptografador Cifra de Cesar")
root.config(padx=50, pady=100)
root.geometry("800x600")


# height = altura
# width = largura
# highlightthickness = espessura destaque

def captura_texto_digitado(entrada_texto:Text):
    texto_digitado = entrada_texto.get(index1="1.0",index2='end-1c')
    print(f'O texto digitado foi {texto_digitado}')

#frame_entrada = Frame(root, width=600, highlightbackground="red", highlightcolor="red", highlightthickness=5, height=250)
frame_entrada = Frame(root, width=600, height=250)
frame_entrada.pack()
frame_entrada.propagate(False)

#frame_entrada_texto = Frame(frame_entrada, width=600, highlightbackground="blue", highlightcolor="blue", highlightthickness=5, height=160)
frame_entrada_texto = Frame(frame_entrada, width=600, height=160)
frame_entrada_texto.pack()
frame_entrada_texto.propagate(False)

entrada_texto = Text(frame_entrada_texto, width=60, height=8)
entrada_texto.pack(anchor="center")

#frame_botao = Frame(frame_entrada, width=470, highlightbackground="green", highlightcolor="green", highlightthickness=5, height=200)
frame_botao = Frame(frame_entrada, width=470,  height=200)
frame_botao.pack()
frame_botao.propagate(False)

botao_cripto = Button(frame_botao, width=25, height=3, text="Clique aqui para criptografar", command=lambda:captura_texto_digitado(entrada_texto))
botao_cripto.pack(side="right")

botao_descripto = Button(frame_botao, width=25, height=3, text="Clique aqui para descriptografar")
botao_descripto.pack(side="left")

#frame_saida = Frame(root, width=600, highlightbackground="green", highlightcolor="green", highlightthickness=5, height=160)
frame_saida = Frame(root, width=600, height=160)
frame_saida.pack()

#frame_saida_texto = Frame(frame_saida, width=600, highlightbackground="red", highlightcolor="red", highlightthickness=5, height=400)
frame_saida_texto = Frame(frame_saida, width=600, height=400)
frame_saida_texto.pack()
frame_saida_texto.propagate(False)

saida_texto = Text(frame_saida_texto, width=60, height=8)
saida_texto.pack(anchor="center")

frame_saida.propagate(False)

root.mainloop()
