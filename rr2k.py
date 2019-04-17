#!/usr/bin/python3
# Arquivo : r2k.py
# Programa: romaji to kana
# Autor   : Rahul Martim Juliato
# Versão  : 0.1  -  27.04.2018


#---===[0. Bibliotecas]===---
import romkan
import tkinter as tk
from tkinter import messagebox as mb
from tkinter import ttk
#---===[0. Fim das Bibliotecas]===---


#---===[0.5 Variáveis Globais]===---
#---===[0.5 Fim das Variáveis Globais]===---


#---===[1. Funções]===---
def quit():
    """ Sai do programa destruindo o necessário
    """
    global janela
    janela.destroy()

def sobre():
    """ Mostra as informações do programa
    """
    mb.showinfo("rr2kX",'''

r[r2k]X
Conversor de Romaji para Kana

Versão: 0.1

Autor: Rahul Martim Juliato
(rahul.juliato@gmail.com)

''')


def erro(mensagem):
    """Sobre uma messagebox de erro com a mensagem
    passada"""
    mb.showerror("Erro!", mensagem)



def converter():
    frase = ent_romaji.get()

    ent_hiraga.delete(0, tk.END)
    ent_hiraga.insert(0, romkan.to_hiragana(frase))

    ent_kataka.delete(0, tk.END)
    ent_kataka.insert(0, romkan.to_katakana(frase))

    pass

    
#---===[1. Fim das Funções]===---



#---===[2. Início da geração da Janela]===---
# 2.0. Definições principais da janela
janela = tk.Tk()
#janela.geometry("500x200")
janela.wm_title('rr2kX v0.1')
janela.wm_minsize(380,180)
janela.grid_anchor(anchor='c')
#janela.tk_setPalette('gray')


# 2.0. Barra de menu
barramenu = tk.Menu(janela)
arquivo = tk.Menu(barramenu, tearoff=800)
arquivo.add_command(label="Sobre", command=sobre)
arquivo.add_separator()
arquivo.add_command(label="Sair", command=quit)
barramenu.add_cascade(label="Arquivo", menu=arquivo)

                    
janela.config(menu=barramenu)

# 2.0 Título dentro da janela principal
titulo = tk.Label(janela, text="R ひ カ", font="Arial 16 bold", height=2)
titulo.grid(column = 0, row = 0, sticky="NSEW", columnspan = '3')


separador = tk.ttk.Separator()
separador.grid(sticky = 'EW', pady = 3, columnspan = '3')

lab_romaji = tk.Label(janela, text="Romaji: ")
lab_romaji.grid(column = 0, row = 2, sticky="E")

ent_romaji = tk.Entry(janela)
ent_romaji.grid(column = 1, row = 2)

bot_conver = tk.Button(janela, text="Converter", command = converter)
bot_conver.grid(column = 2, row = 2)

separador = tk.ttk.Separator()
separador.grid(sticky = 'EW', pady = 10, columnspan = '3')

lab_hiraga = tk.Label(janela, text="Hiragana: ")
lab_hiraga.grid(column = 0, row = 4, sticky="E")

ent_hiraga = tk.Entry(janela, width = 35)
ent_hiraga.grid(column = 1, row = 4, columnspan = '2', sticky = 'W')

lab_kataka = tk.Label(janela, text="Katakana: ")
lab_kataka.grid(column = 0, row = 5, sticky="E")

ent_kataka = tk.Entry(janela, width = 35)
ent_kataka.grid(column = 1, row = 5, columnspan = '2', sticky = 'W')



tk.mainloop()
#---===[2 Fim da Geração da Janela]===---
