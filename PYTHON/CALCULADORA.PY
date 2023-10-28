# importando tkinter
from tkinter import *
from tkinter import ttk

# cores

cor1 = '#1e1f1e'  # cor preta


# Criando janela
janela = Tk()
janela.title = ("Calculadora")

# Definir tamanho da janela
janela.geometry("335x418")

# definir cor da janela
janela.configure(bg=cor1)

# Divisão de tela
frame_tela = Frame(janela, width=335, height=90)
frame_tela.grid(row=0, column=0)


# Criando main loop (que seria a aplicação)
janela.mainloop()
