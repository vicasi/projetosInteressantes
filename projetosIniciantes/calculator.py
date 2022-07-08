from lib2to3.pytree import convert
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import re
import math

minha_janela = tk.Tk()
minha_entrada = tk.Entry()

def submit():
    print(minha_entrada.get())
minha_label = tk.Label(
    text="faça suas contas \o/",
    background='white',
    foreground='purple',
    font=("Verdana", 25)

)

def padrao_sinal(texto):
    padrao_sinal = r"[\+|\-|\*|\/|\*\*|sqrt]"
    regex_sinal = re.findall(padrao_sinal, texto)
    string = "".join(regex_sinal)
    return string



def calculo():
    texto = minha_entrada.get()
    padrao_num0 = r"^\d+\s*"
    padrao_num1 = r"\s*\d+$"
    regex0 = re.findall(padrao_num0, texto)
    regex1 = re.findall(padrao_num1, texto)
    # convert0 = list(map(int, regex0))
    # convert1 = list(map(int, regex1))
    lista_str0 = [str(integer) for integer in regex0]
    lista_str1 = [str(integer) for integer in regex1]
    str0 = "".join(lista_str0)
    str1 = "".join(lista_str1)
    convert0 = int(str0)
    convert1 = int(str1)
    sinal = padrao_sinal(texto)
    if sinal == '*':
        resultado = convert0 * convert1
        return resultado
    elif sinal == '/':
        resultado = convert0 / convert1
        return resultado
    elif sinal == '-':
        resultado = convert0 - convert1
        return resultado
    elif sinal == "+":
        resultado = convert0 + convert1
        return resultado
    elif sinal == '**':
        resultado = math.pow(convert0, convert1)
        return resultado
    elif sinal == 'sqrt':
        resultado = math.sqrt(convert0)
        return resultado
    else:
        return 'valor nao encontrado'


def resultado():
    messagebox.showinfo('resultado',calculo())



meu_botao = tk.Button(text='somar',command=submit)
meu_botao2 = tk.Button(text='resultado',command=resultado)

#packs
minha_label.pack()
minha_entrada.pack()
meu_botao.pack()
meu_botao2.pack()










#loop
minha_janela.mainloop()