import tkinter
class Program:
    def __init__(self):
        """Otvori vsetky obrazky postaviciek a spusti vstupne dialogove okno s vyberom moznosti hry."""
        self.pocethracovs = None
        self.meno = None
        self.prva = 1
        self.pocetulozenych_hracov = 0
        self.auto = tkinter.PhotoImage(file=r"auto.png")
        self.bota = tkinter.PhotoImage(file=r"bota.png")
        self.furik = tkinter.PhotoImage(file=r"furik.png")
        self.klobuk = tkinter.PhotoImage(file=r"klobuk.png")
        self.lod = tkinter.PhotoImage(file=r"lod.png")
        self.macka = tkinter.PhotoImage(file=r"macka.png")
        canvas.create_text(600, 450, text="Víta vás Belo games", font="Arial 40")
        self.novahra = tkinter.Button(text="Nová hra", command=self.zaciatok)
        self.novahra.place(x=500, y=500)
        self.rozohratapartia = tkinter.Button(text="Uložené hry")
        self.rozohratapartia.place(x=600, y=500)

    def start(self):
        """Spusti Vykreslovanie hriacej plochy."""
        print(self.hraci)
        self.startB.place_forget()
        canvas.create_rectangle(110, 110, 704, 704, )
        canvas.create_text(402, 402, text="Belo Games", font="arial 100")
        self.x = 10
        self.y = 110
        canvas.create_rectangle(10, 10, 804, 804)
        canvas.update()
        canvas.after(10)
        canvas.create_rectangle(self.x, self.y, self.x + 100, self.y)
        zoz = ["orange", "orange", None, "orange", None, "deeppink", "deeppink", None, "deeppink"]
        for i in zoz:
            canvas.create_rectangle(10, self.y, 110, self.y + 66)
            if i is not None:
                canvas.create_rectangle(86, self.y, 110, self.y + 66, fill=i)
            self.y += 66
            canvas.update()
            canvas.after(10)

        canvas.create_rectangle(10, self.y, 110, self.y + 100)
        self.x += 100
        zoz = ["blue", "blue", None, "blue", None, None, "brown", None, "brown"]
        for i in zoz:
            canvas.create_rectangle(self.x, self.y, self.x + 66, self.y + 100)
            if i is not None:
                canvas.create_rectangle(self.x, self.y + 20, self.x + 66, self.y, fill=i)
            self.x += 66
            canvas.update()
            canvas.after(10)
        canvas.create_rectangle(self.x, self.y, self.x + 100, self.y + 100)
        self.x += 100
        zoz = ["purple", None, "purple", None, None, "green", None, "green", "green", ]
        for i in zoz:
            canvas.create_rectangle(self.x, self.y, self.x - 100, self.y - 66)
            if i is not None:
                canvas.create_rectangle(self.x - 66, self.y, self.x - 100, self.y - 66, fill=i)
            self.y -= 66
            canvas.update()
            canvas.after(10)
        canvas.create_rectangle(self.x, self.y, self.x - 100, self.y - 100)
        self.x -= 100
        zoz = ["yellow", None, "yellow", "yellow", None, "red", "red", None, "red"]
        for i in zoz:
            canvas.create_rectangle(self.x, self.y, self.x - 66, self.y - 100)
            if i is not None:
                canvas.create_rectangle(self.x, self.y - 20, self.x - 66, self.y, fill=i)
            self.x -= 66
            canvas.update()
            canvas.after(10)

    def butons(self, ):
        """Spusti sa na konci vyberu hraca ako vyzva pre zacatie hry"""
        self.startB = tkinter.Button(text='Štart', command=self.start)
        self.startB.place(x=500, y=600, )

    def zaciatok(self):
        """Vyzva pre vyber poctu hracov cez scale
        plus vytvori dict s vsetkmi podstatnymi info o hracovi kedze ide o novu hru"""
        self.novahra.place_forget()
        self.rozohratapartia.place_forget()
        canvas.create_text(580, 500, text="Vyberte pocet hráčov", font="Arial 20")
        self.pocethracovs = tkinter.Scale(orient='horizontal', from_=2, to=6, length=200)
        self.pocethracovs.place(x=500, y=550)
        self.show_potvrdit()
        self.hraci = {"Hrac1": {"meno": "", "postavicka": "", "karticky": [], "Money": 0},
                      "Hrac2": {"meno": "", "postavicka": "", "karticky": [], "Money": 0},
                      "Hrac3": {"meno": "", "postavicka": "", "karticky": [], "Money": 0},
                      "Hrac4": {"meno": "", "postavicka": "", "karticky": [], "Money": 0},
                      "Hrac5": {"meno": "", "postavicka": "", "karticky": [], "Money": 0},
                      "Hrac6": {"meno": "", "postavicka": "", "karticky": [], "Money": 0},
                      "Hrac7": {"meno": "", "postavicka": "", "karticky": [], "Money": 0},
                      "Hrac8": {"meno": "", "postavicka": "", "karticky": [], "Money": 0},
                      }

    def vyber_postavicky(self):
        """"Zobrazi galeriu postaviciek a moznostou vyberu postavicky."""
        self.autobut = tkinter.Button(text='auto', image=self.auto, command=lambda: self.postavicka_k_hracovi("auto"))
        self.autobut.place(x=900, y=500)
        self.botabut = tkinter.Button(text='bota', image=self.bota, command=lambda: self.postavicka_k_hracovi("bota"))
        self.botabut.place(x=1000, y=500)
        self.furikbut = tkinter.Button(text='Furik', image=self.furik,
                                       command=lambda: self.postavicka_k_hracovi("furik"))
        self.furikbut.place(x=1100, y=500)
        self.klobukbut = tkinter.Button(text='klobuk', image=self.klobuk,
                                        command=lambda: self.postavicka_k_hracovi("klobuk"))
        self.klobukbut.place(x=900, y=400)
        self.lodbut = tkinter.Button(text='lod', image=self.lod, command=lambda: self.postavicka_k_hracovi("lod"))
        self.lodbut.place(x=1000, y=400)
        self.mackabut = tkinter.Button(text='macka', image=self.macka,
                                       command=lambda: self.postavicka_k_hracovi("macka"))
        self.mackabut.place(x=1100, y=400)
        self.prva = 0

    def show_potvrdit(self):
        """Ukaze sa tlacidlo potvrdit s vyzvou na potvrdenie a ulozenie danej veci """
        self.potvrdit = tkinter.Button(text='Potvrdit', command=self.ukladanie)
        self.potvrdit.place(y=600, x=500)

    def ukladanie(self):
        """Ked je spustena prvy krat zavola funkciu ktora zobrazi galeriu postaviciek
        a ulozi info ktore sme dostali o pocte hracov
        ked je spustana znova tak uklada informacie o hracovi ktore si zadal"""
        if self.prva == 1:
            self.vyber_postavicky()
            self.prva = None
            self.pocethracov = self.pocethracovs.get()
            self.pocethracovs.place_forget()
            self.vyber_hracov()
        else:
            hrac = "Hrac" + str(self.pocetulozenych_hracov + 1)
            self.hraci[hrac]["meno"] = self.meno.get()
            self.meno.place_forget()
            self.pocetulozenych_hracov += 1
            if self.pocetulozenych_hracov < self.pocethracov:
                self.vyber_hracov()

            elif self.pocetulozenych_hracov == self.pocethracov:
                canvas.delete("all")
                self.meno.place_forget()
                self.potvrdit.place_forget()
                self.vymaz_tlacitka()

    def vymaz_tlacitka(self):
        """Vymaze vsetky zvysne tlacitka a zavola funkciu na zobrazenie tlacidla START"""
        self.botabut.place_forget()
        self.autobut.place_forget()
        self.mackabut.place_forget()
        self.lodbut.place_forget()
        self.klobukbut.place_forget()
        self.furikbut.place_forget()
        self.butons()

    def postavicka_k_hracovi(self, postavicka):
        """Zmaze prislusny obrazok postavicky, ktora bola vybrana
        a do dict daneho hraca priradi jej meno"""
        self.show_potvrdit()
        if postavicka == "auto":
            self.autobut.place_forget()
        elif postavicka == "bota":
            self.botabut.place_forget()
        elif postavicka == "macka":
            self.mackabut.place_forget()
        elif postavicka == "lod":
            self.lodbut.place_forget()
        elif postavicka == "furik":
            self.furikbut.place_forget()
        elif postavicka == "klobuk":
            self.klobukbut.place_forget()
        hrac = "Hrac" + str(self.pocetulozenych_hracov + 1)
        self.hraci[hrac]["postavicka"] = str(postavicka)

    def vyber_hracov(self):
        """Zobratuje Entry label na zadanie mena hraca"""
        self.potvrdit.place_forget()
        canvas.delete("all")
        canvas.create_text(500, 500,
                           text=f'zadajte meno pre '
                                f'{self.pocetulozenych_hracov + 1}. hráča a vyberte postavicku',
                           font="Arial 20")
        self.meno = tkinter.Entry(width=15, )
        self.meno.place(x=500, y=550)


root = tkinter.Tk()
root.attributes('-fullscreen', True)  # make main window full-screen
canvas = tkinter.Canvas(root)
canvas.pack(fill=tkinter.BOTH, expand=True, )
x = Program()
canvas.mainloop()
