from tkinter import Label, Button, Entry, Tk, Frame, PhotoImage
import qrcode
from PIL import Image, ImageTk
from tkinter import messagebox
import pyshorteners

root = Tk()
root.title("Gerador de Código QR")
root.config(padx=50, pady=100)
    
def create_image_window(root: Tk, image_path: str):
    frame_image = Frame(root, highlightbackground="green", highlightcolor="green", highlightthickness=1, width=400, height=450, bd= 2)
    frame_image.pack(side='right')
    frame_image.propagate(False)
    img = Image.open(image_path)
    tk_img = ImageTk.PhotoImage(img)
    label = Label(frame_image, image=tk_img)
    label.grid(row=2, column=1, columnspan=2)
    label.pack()
    add_button = Button(frame_image, text="Gerar Novo", width=36, command=lambda: voltar_tela_inicial(root))
    add_button.grid(row=4, column=1, columnspan=2)
    add_button.pack()
    root.mainloop()

def gera_qr_code(root: Tk, main_entry: Entry):
    url = main_entry.get()
    if len(url) == 0:
        messagebox.showinfo(title="Erro!",message="Favor insira uma URL válida")
    else:
        main_entry.delete(0, 'end')
        opcao_escolhida = messagebox.askokcancel(
        title=url,
        message=f"O endereço URL é: \n "
                f"Endereço: {url} \n "
                f"Pronto para salvar?")

    if opcao_escolhida:
      qr = qrcode.QRCode(version=1, box_size=10, border=5)
      short_url = pyshorteners.Shortener().tinyurl.short(url)
      qr.add_data(short_url)
      qr.make(fit=True)
      img = qr.make_image(
          fill_color='black', 
          back_color='white'
          )
      img.save('qrExport.png')
      create_image_window(root, 'qrExport.png')

def create_main(root: Tk):
    frame_main = Frame(root, highlightbackground="green", highlightcolor="green", highlightthickness=1, width=400, height=150, bd= 2)
    frame_main.pack(side='left')
    frame_main.propagate(False)
    main_label = Label(frame_main, text="URL:")
    main_label.grid(row=2, column=0)
    main_label.pack()
    main_entry = Entry(frame_main, width=35)
    main_entry.grid(row=2, column=1, columnspan=2)
    main_entry.focus()
    main_entry.pack()
    add_button = Button(frame_main, text="Gerar QR Code", width=36, command=lambda: gera_qr_code(root, main_entry))
    add_button.grid(row=4, column=1, columnspan=2)
    add_button.pack()
    root.mainloop()
    
def voltar_tela_inicial(root: Tk):
    root.destroy()
    root = Tk()
    root.title("Gerador de Código QR")
    root.config(padx=10, pady=100)
    create_main(root)
    
create_main(root)
