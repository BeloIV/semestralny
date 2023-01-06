import tkinter
from PIL import Image, ImageTk
import json


class Program:
    def __init__(self):
        """
        Otvori vsetky obrazky postaviciek a spusti vstupne dialogove okno s vyberom moznosti hry.
        """
        self.karticky = json.load(open('subor.txt'))
        self.pocethracovs = None
        self.meno = None
        self.prva = 1
        self.pocetulozenych_hracov = 0
        self.auto = tkinter.PhotoImage(file=r"Images/auto.png")
        self.bota = tkinter.PhotoImage(file=r"Images/bota.png")
        self.furik = tkinter.PhotoImage(file=r"Images/furik.png")
        self.klobuk = tkinter.PhotoImage(file=r"Images/klobuk.png")
        self.lod = tkinter.PhotoImage(file=r"Images/lod.png")
        self.macka = tkinter.PhotoImage(file=r"Images/macka.png")
        canvas.create_text(600, 450, text="Víta vás Belo games", font="Arial 40")
        vezenie = Image.open(r"Images/vezenie.jpg")
        self.vezenie = ImageTk.PhotoImage(vezenie)
        self.novahra = tkinter.Button(text="Nová hra", command=self.zaciatok)
        self.novahra.place(x=500, y=500)
        self.rozohratapartia = tkinter.Button(text="Uložené hry")
        self.rozohratapartia.place(x=600, y=500)
        vezenie = Image.open(r"Images/vezenie.jpg")
        self.vezenie = ImageTk.PhotoImage(vezenie)
        policajt = Image.open(r"Images/policajt.png")
        policajt = policajt.rotate(-45)
        self.policajt = ImageTk.PhotoImage(policajt)
        wifi = Image.open(r"Images/wifi.png")
        wifi = wifi.rotate(45)
        self.wifi = ImageTk.PhotoImage(wifi)

    def start(self):
        """Spusti Vykreslovanie hriacej plochy."""
        self.startB.place_forget()
        canvas.create_rectangle(110, 110, 704, 704, )
        # noinspection PyArgumentList
        canvas.create_text(402, 402, text="Belo Games", font="arial 100", angle=45)
        self.x = 10
        self.y = 110
        canvas.create_rectangle(10, 10, 804, 804)
        canvas.update()
        canvas.after(10)
        canvas.create_rectangle(self.x, self.y, self.x + 100, self.y)
        pocitac = 0
        kam = 1
        for i in self.karticky["postuponost"]:
            if i == "zeleznica":
                zeleznica = Image.open(f'Images/{self.karticky[i]["Image"]}')
                self.zeleznica1 = zeleznica.rotate(-90)
                self.zeleznica2 = zeleznica.rotate(0)
                self.zeleznica3 = zeleznica.rotate(90)
                self.zeleznica1 = ImageTk.PhotoImage(self.zeleznica1)
                self.zeleznica2 = ImageTk.PhotoImage(self.zeleznica2)
                self.zeleznica3 = ImageTk.PhotoImage(self.zeleznica3)
            elif i == "Pokladna":
                pokladna = Image.open(f'Images/{self.karticky[i]["Image"]}')
                self.pokladna2 = pokladna.rotate(0)
                self.pokladna1 = pokladna.rotate(-90)
                self.pokladna3 = pokladna.rotate(90)
                self.pokladna1 = ImageTk.PhotoImage(self.pokladna1)
                self.pokladna2 = ImageTk.PhotoImage(self.pokladna2)
                self.pokladna3 = ImageTk.PhotoImage(self.pokladna3)
            if i == "Energeticke zavody":
                elektro = Image.open(f'Images/{self.karticky[i]["Image"]}')
                self.elektro1 = elektro.rotate(-90)
                self.elektro2 = elektro.rotate(0)
                self.elektro3 = elektro.rotate(90)
                self.elektro1 = ImageTk.PhotoImage(self.elektro1)
                self.elektro2 = ImageTk.PhotoImage(self.elektro2)
                self.elektro3 = ImageTk.PhotoImage(self.elektro3)
            elif i == "Sanca":
                sanca = Image.open(f'Images/{self.karticky[i]["Image"]}')
                self.sanca1 = sanca.rotate(-90)
                self.sanca2 = sanca.rotate(0)
                self.sanca3 = sanca.rotate(90)
                self.sanca1 = ImageTk.PhotoImage(self.sanca1)
                self.sanca2 = ImageTk.PhotoImage(self.sanca2)
                self.sanca3 = ImageTk.PhotoImage(self.sanca3)
            elif i == "Vodarne":
                voda = Image.open(f'Images/{self.karticky[i]["Image"]}')
                self.voda1 = voda.rotate(-90)
                self.voda2 = voda.rotate(0)
                self.voda3 = voda.rotate(90)
                self.voda1 = ImageTk.PhotoImage(self.voda1)
                self.voda2 = ImageTk.PhotoImage(self.voda2)
                self.voda3 = ImageTk.PhotoImage(self.voda3)

        for cis, i in enumerate(self.karticky["postuponost"]):
            if kam == 1:
                angl = -90
                anlx = 10
                angly = 33
                plusx = 100
                plusy = 66
                plusnafarbux = 66
                plusnafarbuy = 0
                posunx = 0
                posuny = 66
                zatackax = 100
                zatackay = 0
                farbax = 100
                farbay = 66
                sancax = 33
                sancay = 40
                pokladnax = 60
                pokladnay = 33
                zeleznicax = 60
                zeleznicay = 33
            if kam == 2:
                angl = 0
                anlx = 33
                angly = 90
                plusx = 66
                plusy = 100
                plusnafarbux = 0
                plusnafarbuy = 34
                farbax = 66
                farbay = 0
                posunx = 66
                posuny = 0
                sancax = 33
                sancay = 40
                pokladnax = 33
                pokladnay = 40
                zeleznicax = 33
                zeleznicay = 40
            elif kam == 3:
                angl = 90
                anlx = -10
                angly = -33
                plusx = -100
                plusy = -66
                plusnafarbux = -66
                plusnafarbuy = 0
                zatackax = -100
                zatackay = 0
                farbax = -100
                farbay = -66
                posunx = 0
                posuny = -66
                sancax = -55
                sancay = -33
                pokladnax = -60
                pokladnay = -33
                zeleznicax = -60
                zeleznicay = -30
            elif kam == 4:
                angl = 0
                anlx = -33
                angly = -90
                plusx = -66
                plusy = -100
                plusnafarbux = 0
                plusnafarbuy = -34
                farbax = -66
                farbay = 0
                posunx = -66
                posuny = 0
                sancax = -33
                sancay = -50
                zeleznicax = -33
                zeleznicay = -50
            canvas.create_rectangle(self.x, self.y, self.x + plusx, self.y + plusy)
            canvas.update()
            canvas.after(100)
            self.karticky[i]["indexod"] = self.x
            self.karticky[i]["indexdo"] = self.x + plusx
            self.karticky[i]["indexyod"] = self.y
            self.karticky[i]["indexydo"] = self.y + plusy
            if self.karticky[i]["Farba"] is not None:
                canvas.create_rectangle(self.x + plusnafarbux, self.y + plusnafarbuy, self.x + farbax, self.y + farbay,
                                        fill=self.karticky[i]["Farba"])
            if self.karticky[i]["Nakupna cena"] is not None:
                canvas.create_text(self.x + anlx, self.y + angly, text=(str(self.karticky[i]["Nakupna cena"]) + "$"),
                                   anchor="center", angle=angl)
            try:
                if self.karticky[i]["Image"] is not None:
                    if i == "zeleznica":

                        if kam == 1:
                            canvas.create_image(self.x + zeleznicax, self.y + zeleznicay, image=self.zeleznica1)
                        elif kam == 2 or kam == 4:
                            canvas.create_image(self.x + zeleznicax, self.y + zeleznicay, image=self.zeleznica2)
                        elif kam == 3:
                            canvas.create_image(self.x + zeleznicax, self.y + zeleznicay, image=self.zeleznica3)
                    elif i == "Pokladna":
                        canvas.create_text(self.x + anlx, self.y + angly, text=self.karticky[i]["Nazov"], angle=angl,
                                           anchor="center")
                        if kam == 1:
                            canvas.create_image(self.x + pokladnax, self.y + pokladnay, image=self.pokladna1)
                        elif kam == 2 or kam == 4:
                            canvas.create_image(self.x + pokladnax, self.y + pokladnay, image=self.pokladna2)
                        elif kam == 3:
                            canvas.create_image(self.x + pokladnax, self.y + pokladnay, image=self.pokladna3)
                    elif i == "Energeticke zavody":
                        if kam == 1:
                            canvas.create_image(self.x + 50, self.y + 33, image=self.elektro1)
                        elif kam == 2 or kam == 4:
                            canvas.create_image(self.x, self.y, image=self.elektro2)
                        elif kam == 3:
                            canvas.create_image(self.x, self.y, image=self.elektro3)
                    elif i == "Sanca":
                        canvas.create_text(self.x + anlx, self.y + angly, text=self.karticky[i]["Nazov"], angle=angl,
                                           anchor="center")
                        if kam == 1:
                            canvas.create_image(self.x + sancax, self.y + sancay, image=self.sanca1)
                        elif kam == 2 or kam == 4:
                            canvas.create_image(self.x + sancax, self.y + sancay, image=self.sanca2)
                        elif kam == 3:
                            canvas.create_image(self.x + sancax, self.y + sancay, image=self.sanca3)
                    elif i == "Vodarne":
                        if kam == 1:
                            canvas.create_image(self.x, self.y, image=self.voda1)
                        elif kam == 2 or kam == 4:
                            canvas.create_image(self.x - 33, self.y - 50, image=self.voda2)
                        elif kam == 3:
                            canvas.create_image(self.x, self.y, image=self.voda3)
            except:
                pass

            if "Dan" in i:
                if kam == 2:
                    canvas.create_text(self.x + anlx, self.y + angly - 40,
                                       text=f'Daň z\nprímu\nzaplate:\n{self.karticky[i]["Zakladne najomne"]} $',
                                       angle=angl,
                                       anchor="center", font="Ariel 15")
                elif kam == 3:
                    canvas.create_text(self.x + anlx - 40, self.y + angly,
                                       text=f'Daň z\nprímu\nzaplate:\n{self.karticky[i]["Zakladne najomne"]} $',
                                       angle=angl,
                                       anchor="center", font="Ariel 15")
            if pocitac == 8:
                self.y += posuny + zatackay
                self.x += zatackax + posunx
                pocitac = 0
                if kam == 1:
                    canvas.create_image(self.x - 40, self.y + 40, image=self.vezenie)
                    canvas.create_text(self.x - 15, self.y + 15, text="Vo ", angle=-45, font="Arial 18", fill="black")
                    canvas.create_text(self.x - 60, self.y + 63, text="väzaní ", angle=-45, font="Arial 15",
                                       fill="black")
                    canvas.create_text(self.x - 90, self.y + 40, text="Iba na ", angle=-90, font="Arial 18")
                    canvas.create_text(self.x - 50, self.y + 90, text="návšteve", font="Arial 18")
                elif kam == 2:
                    canvas.create_text(self.x - 65, self.y + 35, text="Štart", font="Arial 35", angle=45)
                    canvas.create_text(self.x - 45, self.y + 50, text="Ziskávate 200$", font="Arial 15", angle=45)
                elif kam == 3:
                    canvas.create_image(self.x + 50, self.y - 50, image=self.policajt, )
                    canvas.create_text(self.x + 75, self.y - 70, text="Choď do", angle=-45, font="Arial 18")
                    canvas.create_text(self.x + 25, self.y - 25, text="väzenia", angle=-45, font="Arial 18")
                elif kam == 4:
                    canvas.create_image(self.x + 50, self.y - 50, image=self.wifi)
                kam += 1
            else:
                self.y += posuny
                self.x += posunx
                pocitac += 1
        self.ukaz_hracov()

    def ukaz_hracov(self):
        """Ukaže mena a hodnotu majetku hračov """
        print("hi")
        for x, i in enumerate(self.hraci):
            print(x, i)
            images = []  # to hold the newly created image
            image = Image.new('RGBA', (10000, 10000), (65535, 65535, 65535, 127))
            images.append(ImageTk.PhotoImage(image))
            ramram = canvas.create_image(0, 0, image=images[-1], anchor='nw')
            ram = canvas.create_rectangle(300, 300, 500, 500, fill="light blue")
            text = canvas.create_text(400, 350, text=self.hraci[i]["meno"], fill="black", font="Arial 20")
            text1 = canvas.create_text(400, 370, text=f'Majetok: {self.hraci[i]["Money"]}', fill="black",
                                       font="Arial 15")

            if self.hraci[i]["postavicka"] == "auto":
                postavicka=canvas.create_image(400, 420,image=self.auto)

            elif self.hraci[i]["postavicka"] == "bota":
                postavicka=canvas.create_image(400, 420,image=self.bota)
            elif self.hraci[i]["postavicka"] == "macka":
                postavicka=canvas.create_image(400, 420,image=self.macka)
            elif self.hraci[i]["postavicka"] == "lod":
                postavicka=canvas.create_image(400, 420,image=self.lod)
            elif self.hraci[i]["postavicka"] == "furik":
                postavicka=canvas.create_image(400, 420,image=self.furik)
            elif self.hraci[i]["postavicka"] == "klobuk":
                postavicka=canvas.create_image(400, 420,image=self.klobuk)
            canvas.update()
            canvas.after(2000)
            canvas.delete(ram, text, text1,postavicka)
            if x == self.pocethracov - 1:
                canvas.delete(ram,ramram)

                break
    def butons(self, ):
        """Spusti sa na konci vyberu hraca ako vyzva pre zacatie hry"""
        self.startB = tkinter.Button(text='Štart', command=self.start)
        self.startB.place(x=500, y=600, )

    def zaciatok(self):
        """
        Vyzva pre vyber poctu hracov cez scale
        plus vytvori dict s vsetkmi podstatnymi info o hracovi kedze ide o novu hru
        """
        self.novahra.place_forget()
        self.rozohratapartia.place_forget()
        canvas.create_text(580, 500, text="Vyberte pocet hráčov", font="Arial 20")
        self.pocethracovs = tkinter.Scale(orient='horizontal', from_=2, to=6, length=200)
        self.pocethracovs.place(x=500, y=550)
        self.show_potvrdit()
        self.hraci = {"Hrac1": {"meno": "Hrac 1", "postavicka": "", "karticky": [], "Money": 5000},
                      "Hrac2": {"meno": "Hrac 2", "postavicka": "", "karticky": [], "Money": 5000},
                      "Hrac3": {"meno": "Hrac 3", "postavicka": "", "karticky": [], "Money": 5000},
                      "Hrac4": {"meno": "Hrac 4", "postavicka": "", "karticky": [], "Money": 5000},
                      "Hrac5": {"meno": "Hrac 5", "postavicka": "", "karticky": [], "Money": 5000},
                      "Hrac6": {"meno": "Hrac 6", "postavicka": "", "karticky": [], "Money": 5000}, }

    def vyber_postavicky(self):
        """"
        Zobrazi galeriu postaviciek a moznostou vyberu postavicky.
        """
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
        """
        Ukaze sa tlacidlo potvrdit s vyzvou na potvrdenie a ulozenie danej veci
         """
        self.potvrdit = tkinter.Button(text='Potvrdit', command=self.ukladanie)
        self.potvrdit.place(y=600, x=500)

    def ukladanie(self):
        """
        Ked je spustena prvy krat zavola funkciu ktora zobrazi galeriu postaviciek
        a ulozi info ktore sme dostali o pocte hracov
        ked je spustana znova tak uklada informacie o hracovi ktore si zadal
        """
        if self.prva == 1:
            self.vyber_postavicky()
            self.prva = None
            self.pocethracov = self.pocethracovs.get()
            self.pocethracovs.place_forget()
            self.vyber_hracov()
        else:
            hrac = "Hrac" + str(self.pocetulozenych_hracov + 1)
            if self.meno.get() != "":
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
        """
        Vymaze vsetky zvysne tlacitka a zavola funkciu na zobrazenie tlacidla START
        """
        self.botabut.place_forget()
        self.autobut.place_forget()
        self.mackabut.place_forget()
        self.lodbut.place_forget()
        self.klobukbut.place_forget()
        self.furikbut.place_forget()
        self.butons()

    def postavicka_k_hracovi(self, postavicka):
        """
        Zmaze prislusny obrazok postavicky, ktora bola vybrana
        a do dict daneho hraca priradi jej meno
        """
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
        """
        Zobratuje Entry label na zadanie mena hraca
        """
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
