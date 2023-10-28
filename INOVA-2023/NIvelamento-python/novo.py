import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('interface')
nome_label = ttk.Label(root, text="Olá")
nome_label.pack(padx=20, pady=20)

# define tamanho da tela
root.geometry("500x500")

# definir a cor
root.configure(bg='green')

# Definir a fonte
fonte = ('Arial', 52, 'bold')


# criar os widgets

nome_label = ttk.Label(root, text="Nome:", font=fonte)
nome_entry = ttk.Entry(root, font=fonte, width=30)

# nome_labal.pack
nome_label.grig(row=0, column=0, padx=10, pady=5)
nome_entry.grid(row=0, column=1, padx=10, pady=5)

# Adicionar um botão e posicionar a janela
# botao = ttk.Button(root, text="Clique aqui")
# botao.grid(row=1, column=0, columnspan=2, padx=5, pady=10)


# def exibir_mensagem():
# nome = nome_entry.get()
# mensagem_label["text"] = "Olá," + nome


# esta funcionalidade esrá sempre a ultima
root.mainloop()
