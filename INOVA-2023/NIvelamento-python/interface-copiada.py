import tkinter


class appimc_tk(tkinter.Tk):
    def __init__(self, parent):
        tkinter.Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid()
        # titulo
        titulo = tkinter.Label(self, text="Índice de Massa Corporal ",
                               font=("Arial 18 bold"), anchor="center",
                               fg="white", bg="blue")
        titulo.grid(column=0, row=0, columnspan=2, sticky='EW')
        espaco = tkinter.Label(self, text="", anchor="center", bg="snow")
        espaco.grid(column=0, row=1, columnspan=2, sticky='EW')

        # Variáveis Texto
        peso = tkinter.Label(self, text="Peso (em Kg): ", font=("Times 12"),
                             anchor="w", fg="slate gray", bg="cyan")
        peso.grid(column=0, row=2, columnspan=1, sticky='EW')

        altura = tkinter.Label(self, text="Altura (em metros): ", font=("Times 12"),
                               anchor="w", fg="slate gray",
                               bg="light cyan")
        altura.grid(column=0, row=3, columnspan=1, sticky='EW')
        espaco1 = tkinter.Label(self, text="", anchor="center", bg="snow")
        espaco1.grid(column=0, row=4, columnspan=2, sticky='EW')
        # Entradas
        self.kg = tkinter.DoubleVar()
        quilos = tkinter.Entry(self, textvariable=self.kg)
        quilos.grid(column=1, row=2, sticky='EW')

        self.mt = tkinter.DoubleVar()
        metros = tkinter.Entry(self, textvariable=self.mt)
        metros.grid(column=1, row=3, sticky='EW')
        # Butão
        butao = tkinter.Button(
            self, text="Calcular o IMC", command=self.butaoclick)
        butao.grid(column=0, row=5, columnspan=2)

        self.rimc = tkinter.StringVar()
        resultado = tkinter.Label(self, textvariable=self.rimc)
        resultado.grid(column=1, row=6, sticky='EW')
        textoresultado = tkinter.Label(
            self, textvariable=self, text="Seu Índice de Massa Corporal é ")
        textoresultado.grid(column=0, row=6, sticky='EW')

        self.grid_columnconfigure(0, weight=1)
        self.resizable(True, True)

    def butaoclick(self):
        p = self.kg.get()
        a = self.mt.get()
        e = a*a
        mpg = (p/e)
        return self.rimc.set(mpg)


if __name__ == "__main__":
    app = appimc_tk(None)
    app.title('Calculadora do índice de'
              ' massa corporal (IMC)')

app.mainloop()
