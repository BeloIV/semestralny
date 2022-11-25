import time
import tkinter
from PIL import ImageTk, Image
class Program:
    def __init__(self):
        """Otvori vsetky obrazky postaviciek a spusti vstupne dialogove okno s vyberom moznosti hry."""
        self.auto = tkinter.PhotoImage(file=r"auto.png")
        self.bota = tkinter.PhotoImage(file=r"bota.png")
        self.furik = tkinter.PhotoImage(file=r"furik.png")
        self.klobuk = tkinter.PhotoImage(file=r"klobuk.png")
        self.lod = tkinter.PhotoImage(file=r"lod.png")
        self.macka = tkinter.PhotoImage(file=r"macka.png")
        canvas.create_text(600,450,text="Víta vás Belo games",font="Arial 40")
        self.novahra=tkinter.Button(text="Nová hra",command=self.zaciatok)
        self.novahra.place(x=500,y=500)
        self.rozohratapartia=tkinter.Button(text="Uložene hry")
        self.rozohratapartia.place(x=600,y=500)

    def start(self):
        """Spusti Vykreslovanie hriacej plochy."""
        self.startB.place_forget()
        self.x = self.meno.get()
        self.hraci.append(self.x)
        canvas.delete("all")
        self.meno.place_forget()
        canvas.create_rectangle(110,110,704,704,)
        canvas.create_text(402,402,text="Belo Games",font="arial 100")
        self.x = 10
        self.y = 110
        canvas.create_rectangle(10, 10, 804, 804)
        canvas.update()
        canvas.after(10)
        canvas.create_rectangle(self.x, self.y, self.x+100, self.y)
        zoz = ["orange", "orange", None, "orange", None, "deeppink", "deeppink", None, "deeppink"]
        for i in zoz:
            canvas.create_rectangle(10, self.y, 110, self.y + 66)
            if i != None:
                canvas.create_rectangle(86, self.y, 110, self.y + 66, fill=i)
            self.y += 66
            canvas.update()
            canvas.after(10)

        canvas.create_rectangle(10, self.y, 110, self.y + 100)
        self.x += 100
        zoz = ["blue", "blue", None, "blue", None, None, "brown", None, "brown"]
        for i in zoz:
            canvas.create_rectangle(self.x, self.y, self.x + 66, self.y + 100)
            if i != None:
                canvas.create_rectangle(self.x, self.y + 20, self.x + 66, self.y, fill=i)
            self.x += 66
            canvas.update()
            canvas.after(10)
        canvas.create_rectangle(self.x, self.y, self.x + 100, self.y + 100)
        self.x += 100
        zoz=["purple",None,"purple",None,None,"green",None,"green","green",]
        for i in zoz:
            canvas.create_rectangle(self.x, self.y,self.x-100, self.y - 66)
            if i != None:
                canvas.create_rectangle(self.x-66, self.y, self.x-100, self.y - 66, fill=i)
            self.y -= 66
            canvas.update()
            canvas.after(10)
        canvas.create_rectangle(self.x, self.y, self.x-100, self.y-100 )
        self.x -= 100
        zoz=["yellow",None,"yellow","yellow",None,"red","red",None,"red"]
        for i in zoz:
            canvas.create_rectangle(self.x, self.y, self.x - 66, self.y - 100)
            if i != None:
                canvas.create_rectangle(self.x, self.y - 20, self.x - 66, self.y, fill=i)
            self.x -= 66
            canvas.update()
            canvas.after(10)

    def butons(self,):
        """Spusti sa na konci vyberu hraco ako vyzva pre zacatie hry"""
        self.startB = tkinter.Button(text='Štart', command=self.start )
        self.startB.place(x=500, y=600, )


    def zaciatok(self):
        """Vyzva pre vyber poctu hracov.
        a nacitanie mien hracov"""
        self.hraci=[]
        self.postavicky=[]
        self.novahra.place_forget()
        self.rozohratapartia.place_forget()
        canvas.create_text(580,500,text="Vyberte pocet hráčov",font="Arial 20")
        self.pocethracovs=tkinter.Scale(orient='horizontal', from_=2, to=8, length=200)
        self.pocethracovs.place(x=500,y=550)
        self.show_potvrdit()
        self.q=False
    def pocet_hracov(self):

        self.pocethracov = self.pocethracovs.get()
        self.pocethracovs.place_forget()
        self.vyber_hracov()
        self.vyber_postavicky()



    def vyber_postavicky(self):
        """"Zobrazi galeriu postaviciek a moznostou vyberu postavicky."""
        self.potvrdit.place_forget()
        self.autobut = tkinter.Button(text='auto', image=self.auto,command= self.postavicka_k_hracovi)
        self.autobut.place(x=900, y=500)
        self.botabut = tkinter.Button(text='bota', image=self.bota).place(x=1000, y=500)
        self.furokbut = tkinter.Button(text='Furik', image=self.furik).place(x=1100, y=500)
        self.klobukbut = tkinter.Button(text='klobuk', image=self.klobuk).place(x=900, y=400)
        self.lodbut = tkinter.Button(text='lod', image=self.lod).place(x=1000, y=400)
        self.mackabut = tkinter.Button(text='macka', image=self.macka).place(x=1100, y=400)


    def postavicka_k_hracovi(self):
        self.autobut.place_forget()
        self.show_potvrdit()





    def show_potvrdit(self):
        self.potvrdit = tkinter.Button(text='Potvrdit', command=self.pocet_hracov, )
        self.potvrdit.place(y=600, x=500)


    def vyber_hracov(self):
        """Zobratuje Entry label na zadanie mena hraca"""
        if self.q:
            self.x = self.meno.get()
            self.hraci.append(self.x)
            self.meno.place_forget()
        if len(self.hraci)==self.pocethracov-1:
            self.potvrdit.place_forget()
            canvas.delete("all")
            self.vyber_postavicky()
            canvas.create_text(500, 500, text=f'zadajte meno pre {len(self.hraci) + 1}. hráča a vyberte postavicku',font="Arial 20")
            self.meno = tkinter.Entry(width=15,)
            self.meno.place(x=500, y=550)
            self.butons()
        elif len(self.hraci)<=self.pocethracov:
            canvas.delete("all")
            self.vyber_postavicky()
            canvas.create_text(500,500,text=f'zadajte meno pre {len(self.hraci)+1}. hráča a vyberte postavicku',font="Arial 20")
            self.meno=tkinter.Entry(width=15)
            self.meno.place(x=500,y=550)
            self.q=True





root = tkinter.Tk()
root.attributes('-fullscreen', True) # make main window full-screen
canvas = tkinter.Canvas(root)
canvas=tkinter.Canvas()
canvas.pack(fill=tkinter.BOTH, expand=True,)
x=Program()
canvas.mainloop()