import tkinter as tk
from tkinter import ttk

minha_janela = tk.Tk()
minha_entrada = tk.Entry()

def submit():
    print(minha_entrada.get())
minha_label = tk.Label(
    text="Olá mundo! \o/",
    background='white',
    foreground='purple',
    font=("Verdana", 25)

)


meu_botao = tk.Button(text='somar',command=submit)
meu_botao2 = tk.Button(text='somar',command=submit)


#packs
minha_label.pack()
minha_entrada.pack()
meu_botao.pack()
meu_botao2.pack()










#loop
minha_janela.mainloop()