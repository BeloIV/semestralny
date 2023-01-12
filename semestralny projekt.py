import tkinter
import random
from PIL import Image, ImageTk
import json


class Program():

    def __init__(self):
        """
        ulozi potrebne premenne .
        """
        self.pocethracovs = None
        self.meno = None
        self.prva = 1
        self.pocetulozenych_hracov = 0
        self.openeverithing()
        self.ram = None
        self.mozes = 1
        self.uvodny_screen()
        self.zoznamhracov = []
        self.ktoide = None


    def openeverithing(self):

        """
        Otvori vsetky subory v programe
        """
        self.karticky = json.load(open('subor.txt'))
        self.dom = Image.open(r"Images/dom.png")
        self.hotel = Image.open(r"Images/hotel.png")
        self.ximg = tkinter.PhotoImage(file=r"Images/close2.png")
        self.elektrorr = Image.open(r"Images/elektro2.png")
        self.vlak = Image.open(r"Images/vlak2.png")
        self.kohutik = Image.open(r"Images/kohutik2.png")
        self.dan = Image.open(r"Images/dan2.png")
        obr1 = Image.open(f'Images/dice/roll1.png')
        self.kocka1obr = ImageTk.PhotoImage(obr1)
        obr2 = Image.open(f'Images/dice/roll2.png')
        self.kocka2obr = ImageTk.PhotoImage(obr2)
        obr3 = Image.open(f'Images/dice/roll3.png')
        self.kocka3 = ImageTk.PhotoImage(obr3)
        obr4 = Image.open(f'Images/dice/roll4.png')
        self.kocka4 = ImageTk.PhotoImage(obr4)
        obr5 = Image.open(f'Images/dice/roll5.png')
        self.kocka5 = ImageTk.PhotoImage(obr5)
        obr6 = Image.open(f'Images/dice/roll6.png')
        self.kocka6 = ImageTk.PhotoImage(obr6)
        vezenie = Image.open(r"Images/vezenie.jpg")
        self.vezenie = ImageTk.PhotoImage(vezenie)
        policajt = Image.open(r"Images/policajt.png")
        policajt = policajt.rotate(-45)
        self.policajt = ImageTk.PhotoImage(policajt)
        wifi = Image.open(r"Images/wifi.png")
        wifi = wifi.rotate(45)
        self.wifi = ImageTk.PhotoImage(wifi)
        self.auto = Image.open(r"Images/auto.png")
        self.bota = Image.open(r"Images/bota.png")
        self.furik = Image.open(r"Images/furik.png")
        self.klobuk = Image.open(r"Images/klobuk.png")
        self.lod = Image.open(r"Images/lod.png")
        self.macka = Image.open(r"Images/macka.png")
        self.dom = Image.open(r"Images/dom.png")
        self.hotel = Image.open(r"Images/hotel.png")
        self.autou = ImageTk.PhotoImage(self.auto)
        self.botau = ImageTk.PhotoImage(self.bota)
        self.mackau = ImageTk.PhotoImage(self.macka)
        self.lodu = ImageTk.PhotoImage(self.lod)
        self.furiku = ImageTk.PhotoImage(self.furik)
        self.klobuku = ImageTk.PhotoImage(self.klobuk)
        self.zozkociek = [self.kocka1obr, self.kocka2obr, self.kocka3, self.kocka4, self.kocka5, self.kocka6]

    def uvodny_screen(self):
        """Ukaze uvodnu plochu s moznostou vyberu nova hra / ulozene hry"""
        canvas.create_text(600, 450, text="Víta vás Belo games", font="Arial 40")
        self.novahra = tkinter.Button(text="Nová hra", command=self.zaciatok)
        self.novahra.place(x=500, y=500)
        self.rozohratapartia = tkinter.Button(text="Uložené hry")
        self.rozohratapartia.place(x=600, y=500)

    def start(self):
        """Spusti Vykreslovanie hriacej plochy."""
        self.ukladanie()
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
            if "zeleznica" in i:

                zeleznica = Image.open(f'Images/{self.karticky[i]["Image"]}')
                self.zeleznica1 = zeleznica.rotate(-90)
                self.zeleznica2 = zeleznica.rotate(0)
                self.zeleznica3 = zeleznica.rotate(90)
                self.zeleznica1 = ImageTk.PhotoImage(self.zeleznica1)
                self.zeleznica2 = ImageTk.PhotoImage(self.zeleznica2)
                self.zeleznica3 = ImageTk.PhotoImage(self.zeleznica3)
            elif "Pokladna" in i:
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
            elif "Sanca" in i:
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
            self.karticky[i]["odx"] = self.x
            self.karticky[i]["ody"] = self.y
            self.karticky[i]["dox"] = self.x + plusx
            self.karticky[i]["doy"] = self.y + plusy
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
                    if "zeleznica" in i:
                        if kam == 1:
                            canvas.create_image(self.x + zeleznicax, self.y + zeleznicay, image=self.zeleznica1)
                        elif kam == 2 or kam == 4:
                            canvas.create_image(self.x + zeleznicax, self.y + zeleznicay, image=self.zeleznica2)
                        elif kam == 3:
                            canvas.create_image(self.x + zeleznicax, self.y + zeleznicay, image=self.zeleznica3)
                    elif "Pokladna" in i:
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
                    elif "Sanca" in i:
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
        self.polozenie_postaviciek()
        for x, i in enumerate(self.hraci):
            images = []  # to hold the newly created image
            image = Image.new('RGBA', (10000, 10000), (65535, 65535, 65535, 127))
            images.append(ImageTk.PhotoImage(image))
            ramram = canvas.create_image(0, 0, image=images[-1], anchor='nw')
            ram = canvas.create_rectangle(300, 300, 500, 500, fill="light blue")
            text = canvas.create_text(400, 350, text=self.hraci[i]["meno"], fill="black", font="Arial 20")
            text1 = canvas.create_text(400, 370, text=f'Majetok: {self.hraci[i]["Money"]} $ ', fill="black",
                                       font="Arial 15")
            if self.hraci[i]["postavicka"] == "auto":
                postavicka = canvas.create_image(400, 420, image=self.autou)
            elif self.hraci[i]["postavicka"] == "bota":
                postavicka = canvas.create_image(400, 430, image=self.botau)
            elif self.hraci[i]["postavicka"] == "macka":
                postavicka = canvas.create_image(400, 420, image=self.mackau)
            elif self.hraci[i]["postavicka"] == "lod":
                postavicka = canvas.create_image(400, 420, image=self.lodu)
            elif self.hraci[i]["postavicka"] == "furik":
                postavicka = canvas.create_image(400, 420, image=self.furiku)
            elif self.hraci[i]["postavicka"] == "klobuk":
                postavicka = canvas.create_image(400, 420, image=self.klobuku)
            canvas.update()
            canvas.after(1000)
            canvas.delete(ram, text, text1, postavicka)
            if x == self.pocethracov - 1:
                canvas.delete(ram, ramram)
                break
        self.kocka()

    def zaciatok(self):
        """
        Vyzva pre vyber poctu hracov cez scale
        plus vytvori dict s vsetkmi podstatnymi info o hracovi kedze ide o novu hru
        """
        self.novahra.place_forget()
        self.rozohratapartia.place_forget()
        canvas.create_text(580, 500, text="Vyberte počet hráčov", font="Arial 20")
        self.pocethracovs = tkinter.Scale(orient='horizontal', from_=2, to=6, length=200)
        self.pocethracovs.place(x=500, y=550)
        self.show_potvrdit()
        self.hraci = {"Hrac1": {"meno": "Hrac 1", "postavicka": "", "karticky": [], "Money": 5000},
                      "Hrac2": {"meno": "Hrac 2", "postavicka": "", "karticky": [], "Money": 5000},
                      "Hrac3": {"meno": "Hrac 3", "postavicka": "", "karticky": [], "Money": 5000},
                      "Hrac4": {"meno": "Hrac 4", "postavicka": "", "karticky": [], "Money": 5000},
                      "Hrac5": {"meno": "Hrac 5", "postavicka": "", "karticky": [], "Money": 5000},
                      "Hrac6": {"meno": "Hrac 6", "postavicka": "", "karticky": [], "Money": 5000}, }

    def show_potvrdit(self):
        """
        Ukaze sa tlacidlo potvrdit s vyzvou na potvrdenie a ulozenie danej veci
        """
        self.potvrdit = tkinter.Button(text='Potvrdiť', command=self.ukladanie)
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
            self.zoznamhracov.append(hrac)

            self.meno.place_forget()
            self.pocetulozenych_hracov += 1
            if self.pocetulozenych_hracov < self.pocethracov:
                self.vyber_hracov()
            elif self.pocetulozenych_hracov == self.pocethracov:
                canvas.delete("all")
                self.startB.place_forget()
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

    def butons(self, ):
        """Spusti sa na konci vyberu hraca ako vyzva pre zacatie hry"""
        self.startB = tkinter.Button(text='Štart', command=self.start)
        self.startB.place(x=500, y=600, )

    def vyber_hracov(self):
        """
        Zobratuje Entry label na zadanie mena hraca
        """
        self.potvrdit.place_forget()
        canvas.delete("all")
        canvas.create_text(500, 500,
                           text=f'Zadajte meno pre '
                                f'{self.pocetulozenych_hracov + 1}. hráča a vyberte postavicku',
                           font="Arial 20")
        self.meno = tkinter.Entry(width=15, )
        self.meno.place(x=500, y=550)

    def vyber_postavicky(self):
        """"
        Zobrazi galeriu postaviciek a moznostou vyberu postavicky.
        """
        self.autobut = tkinter.Button(text='auto', image=self.autou, command=lambda: self.postavicka_k_hracovi("auto"))
        self.autobut.place(x=900, y=500)
        self.botabut = tkinter.Button(text='bota', image=self.botau, command=lambda: self.postavicka_k_hracovi("bota"))
        self.botabut.place(x=1000, y=500)
        self.furikbut = tkinter.Button(text='Furik', image=self.furiku,
                                       command=lambda: self.postavicka_k_hracovi("furik"))
        self.furikbut.place(x=1100, y=500)
        self.klobukbut = tkinter.Button(text='klobuk', image=self.klobuku,
                                        command=lambda: self.postavicka_k_hracovi("klobuk"))
        self.klobukbut.place(x=900, y=400)
        self.lodbut = tkinter.Button(text='lod', image=self.lodu, command=lambda: self.postavicka_k_hracovi("lod"))
        self.lodbut.place(x=1000, y=400)
        self.mackabut = tkinter.Button(text='macka', image=self.mackau,
                                       command=lambda: self.postavicka_k_hracovi("macka"))
        self.mackabut.place(x=1100, y=400)
        self.prva = 0

    def postavicka_k_hracovi(self, postavicka):
        """
        Zmaze prislusny obrazok postavicky, ktora bola vybrana
        a do dict daneho hraca priradi jej meno
        """
        if self.pocetulozenych_hracov == self.pocethracov - 1:
            self.butons()
        else:
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

    def kocka(self):
        """
        Polozi 2 sestky na miesto s kockami aby neboli prazdne a zavola child triedu
        (info ze sa moze zacat hra t.j plocha je vykreslena)
        """
        Vypis.hra(self)
        self.ramkocky = canvas.create_rectangle(820, 370, 880, 430, width=5)
        self.ramkocky2 = canvas.create_rectangle(820, 470, 880, 530, width=5)
        self.kocka1 = canvas.create_image(850, 400, image=self.kocka6)
        self.kocka2 = canvas.create_image(850, 500, image=self.kocka6)

    def polozenie_postaviciek(self):
        """polozi postavicky hracov na hraciu plochu"""
        for cis, i in enumerate(self.hraci):
            if cis < 2:
                x = 720
            elif cis < 4:
                x = 750
                cis -= 2
            else:
                x = 780
                cis = cis - 4
            if self.hraci[i]["postavicka"] == "":
                break
            if self.hraci[i]["postavicka"] == "auto":
                self.autor = self.auto.resize((50, 50))
                self.autoul = ImageTk.PhotoImage(self.autor)
                self.autoposx = 740 + (cis * 35)
                self.autoposy = x
                self.autopostavicka = canvas.create_image(self.autoposx, self.autoposy, image=self.autoul)
            elif self.hraci[i]["postavicka"] == "bota":
                self.botar = self.bota.resize((50, 50))
                self.botaul = ImageTk.PhotoImage(self.botar)
                self.botapostavicka = canvas.create_image(740 + (cis * 35), x, image=self.botaul)
            elif self.hraci[i]["postavicka"] == "macka":
                self.mackar = self.macka.resize((50, 50))
                self.mackaul = ImageTk.PhotoImage(self.mackar)
                self.mackapostavicka = canvas.create_image(740 + (cis * 35), x, image=self.mackaul)
            elif self.hraci[i]["postavicka"] == "lod":
                self.lodr = self.lod.resize((50, 50))
                self.lodul = ImageTk.PhotoImage(self.lodr)
                self.lodpostavicka = canvas.create_image(740 + (cis * 35), x, image=self.lodul)
            elif self.hraci[i]["postavicka"] == "furik":
                self.furikr = self.furik.resize((50, 50))
                self.furikul = ImageTk.PhotoImage(self.furikr)
                self.furikpostavicka = canvas.create_image(740 + (cis * 35), x, image=self.furikul)
            elif self.hraci[i]["postavicka"] == "klobuk":
                self.klobukr = self.klobuk.resize((50, 50))
                self.klobukul = ImageTk.PhotoImage(self.klobukr)
                self.klobukpostavicka = canvas.create_image(740 + (cis * 35), x, image=self.klobukul)

    def klik(self, event):
        """
        Funkcia zistuje na ktoru karticku sa kliklo
        a nasledne vytvori zvacsenu karticku s plnym popisom
        alebo ked sa kliklo na karticky zavola funkciu roll ktorá
        hodi kockami
         """
        karta = None
        if self.ram is not None:
            for x in self.zoz:
                canvas.delete(x)
            self.buttx.place_forget()
            karta = None
        try:
            if 820 < event.x < 880 and 370 < event.y < 530:
                if self.mozes == 1:
                    self.roll()
            for i in self.karticky["postuponost"]:
                if self.karticky[i]["odx"] > self.karticky[i]["dox"]:
                    odx = self.karticky[i]["dox"]
                    dox = self.karticky[i]["odx"]
                else:
                    dox = self.karticky[i]["dox"]
                    odx = self.karticky[i]["odx"]
                if self.karticky[i]["ody"] > self.karticky[i]["doy"]:
                    ody = self.karticky[i]["doy"]
                    doy = self.karticky[i]["ody"]
                else:
                    doy = self.karticky[i]["doy"]
                    ody = self.karticky[i]["ody"]
                if odx <= event.x < dox and ody <= event.y < \
                        doy:
                    karta = i
        except:
            pass
        if karta is not None and "Sanca" not in karta and "Pokladna" not in karta:
            if "Energeticke zavody" in karta or "Vodarne" in karta:

                self.ram = canvas.create_rectangle(270, 220, 530, 580, fill="white")
                self.text = canvas.create_text(400, 240, text=self.karticky[karta]["Nazov"], fill="black",
                                               font="Arial 25")
                kk = self.karticky[karta]["popis"].split()

                if "Energeticke zavody" in karta:
                    self.elektror = self.elektrorr.resize((200, 200))
                    self.elektrouloz = ImageTk.PhotoImage(self.elektror)
                    self.obrazok = canvas.create_image(400, 400, image=self.elektrouloz)


                else:
                    self.kohutikr = self.kohutik.resize((200, 200))
                    self.kohutikuloz = ImageTk.PhotoImage(self.kohutikr)
                    self.obrazok = canvas.create_image(400, 400, image=self.kohutikuloz)

                pocitadlo = 0
                vypis = ""
                for slovo in kk:
                    if "Ak" in slovo:
                        vypis += "\n" + slovo + " "
                        pocitadlo = 0
                    elif pocitadlo < 20:
                        vypis += slovo + " "
                        pocitadlo += len(slovo) + 1
                    else:
                        vypis += "\n" + slovo + " "
                        pocitadlo = 0
                vypis = vypis.strip()
                self.popis = canvas.create_text(400, 350, text=vypis, fill="black", font="Helvetica 15")
                self.texthypoteka = canvas.create_text(400, 515, text=f'Hypotéka {self.karticky[karta]["Hypoteka"]} $',
                                                       fill="black", font="Helvetica 18")
                self.zoz = [self.ram, self.text, self.popis, self.texthypoteka, self.obrazok]
            elif "zeleznica" in karta:
                self.ram = canvas.create_rectangle(270, 220, 530, 580, fill="white")
                self.text = canvas.create_text(400, 240, text=self.karticky[karta]["Nazov"], fill="black",
                                               font="Arial 25")
                self.vlakr = self.vlak.resize((200, 200))
                self.vlakouloz = ImageTk.PhotoImage(self.vlakr)
                self.vlakra = canvas.create_image(400, 400, image=self.vlakouloz)
                najomne = f'Nájom {str(self.karticky[karta]["Zakladne najomne"])} $'
                self.textnajom = canvas.create_text(400, 280, text=najomne, fill="black", font="Helvetica 20")

                self.stan2 = canvas.create_text(400, 320,
                                                text=f'Ak vlastníte 2 stanice  {self.karticky[karta]["Ak vlastni 2"]} $',
                                                fill="black", font="Helvetica 20")
                self.stan3 = canvas.create_text(400, 350,
                                                text=f'Ak vlastníte 3 stanice {self.karticky[karta]["Ak vlastni 3"]} $',
                                                fill="black", font="Helvetica 20")
                self.stan4 = canvas.create_text(400, 380,
                                                text=f'Ak vlastníte 4 stanice {self.karticky[karta]["Ak vlastni 4"]} $',
                                                fill="black", font="Helvetica 20")
                self.texthypoteka = canvas.create_text(400, 515, text=f'Hypotéka {self.karticky[karta]["Hypoteka"]} $',
                                                       fill="black", font="Helvetica 18")
                self.zoz = [self.ram, self.text, self.vlakra, self.textnajom, self.stan4, self.stan3, self.stan2,
                            self.texthypoteka]
            elif "Dan" in karta:
                self.ram = canvas.create_rectangle(270, 220, 530, 580, fill="white")
                self.text = canvas.create_text(400, 240, text=self.karticky[karta]["Nazov"], fill="black",
                                               font="Arial 25")
                self.danouloz = ImageTk.PhotoImage(self.dan)
                self.danu = canvas.create_image(400, 400, image=self.danouloz)
                self.zaplat = canvas.create_text(400, 500, text=f'Zaplať {self.karticky[karta]["Zakladne najomne"]} $',
                                                 fill="black",
                                                 font="Arial 25")
                self.zoz = [self.ram, self.text, self.danu, self.zaplat]
            elif "Sanca" not in karta and "zeleznica" not in karta and "Energeticke zavody" not in karta and "Vodarne" not in karta:
                self.ram = canvas.create_rectangle(270, 220, 530, 580, fill=self.karticky[karta]["Farba"])
                self.podklad = canvas.create_rectangle(300, 260, 500, 540, fill="white")
                najomne = f'Nájom {str(self.karticky[karta]["Zakladne najomne"])} $'
                self.textnajom = canvas.create_text(400, 280, text=najomne, fill="black", font="Helvetica 20")
                self.textnajompozn = canvas.create_text(400, 305,
                                                        text="Nájom sa zdvojnasobuje ak vlastníte\n        všetky budovy z tejto farby.",
                                                        fill="grey", font="Helvetica 12")
                self.domr = self.dom.resize((25, 25))
                self.domuloz = ImageTk.PhotoImage(self.domr)
                self.hotelr = self.hotel.resize((30, 23))
                self.hoteluloz = ImageTk.PhotoImage(self.hotelr)
                self.dom1 = canvas.create_image(330, 350, image=self.domuloz)
                self.dom2 = canvas.create_image(330, 380, image=self.domuloz)
                self.dom3 = canvas.create_image(355, 380, image=self.domuloz)
                self.dom4 = canvas.create_image(330, 410, image=self.domuloz)
                self.dom5 = canvas.create_image(355, 410, image=self.domuloz)
                self.dom6 = canvas.create_image(380, 410, image=self.domuloz)
                self.dom7 = canvas.create_image(330, 440, image=self.domuloz)
                self.dom8 = canvas.create_image(355, 440, image=self.domuloz)
                self.dom9 = canvas.create_image(380, 440, image=self.domuloz)
                self.dom10 = canvas.create_image(405, 440, image=self.domuloz)
                self.hotel1 = canvas.create_image(330, 470, image=self.hoteluloz)
                self.textnajom1d = canvas.create_text((490 - (len(str(self.karticky[karta]["1 dom"])) * 3)), 355,
                                                      text=f'{str(self.karticky[karta]["1 dom"])} $', fill="black",
                                                      font="Arial 15")

                self.textnajom2d = canvas.create_text((490 - (len(str(self.karticky[karta]["2 domy"])) * 3)), 385,
                                                      text=f'{str(self.karticky[karta]["2 domy"])} $',
                                                      fill="black", font="Arial 15")
                self.textnajom3d = canvas.create_text((490 - (len(str(self.karticky[karta]["3 domy"])) * 3)), 415,
                                                      text=f'{str(self.karticky[karta]["3 domy"])} $',
                                                      fill="black", font="Arial 15")
                self.textnajom4d = canvas.create_text((490 - (len(str(self.karticky[karta]["4 domy "])) * 3)), 445,
                                                      text=f'{str(self.karticky[karta]["4 domy "])} $',
                                                      fill="black", font="Arial 15")
                self.textnajomhotel = canvas.create_text((490 - (len(str(self.karticky[karta]["Hotel"])) * 3)), 475,
                                                         text=f'{str(self.karticky[karta]["Hotel"])} $',
                                                         fill="black", font="Arial 15")
                self.textstavba = canvas.create_text(400, 490,
                                                     text=f'Stavba {self.karticky[karta]["Cena domu"]} $ každý.',
                                                     fill="grey", font="Helvetica 15")
                self.texthypoteka = canvas.create_text(400, 515, text=f'Hypotéka {self.karticky[karta]["Hypoteka"]} $',
                                                       fill="black", font="Helvetica 18")
                self.text = canvas.create_text(400, 240, text=self.karticky[karta]["Nazov"], fill="white",
                                               font="Arial 25")
                self.zoz = [self.ram, self.text, self.textnajom, self.podklad, self.dom1, self.dom2,
                            self.dom3, self.dom4, self.dom5, self.dom6, self.dom7, self.dom8, self.dom9, self.dom10,
                            self.hotel1, self.textnajom1d, self.textnajom2d, self.textnajom3d, self.textnajom4d,
                            self.textnajomhotel, self.texthypoteka, self.textstavba, self.textnajompozn]
            self.buttx = tkinter.Button(text="X", command=self.vymaz, image=self.ximg)
            self.buttx.place(x=350, y=590)

    def roll(self):
        """Hadze kockami a na konci ulozi ake cislo bolo na kockách"""
        self.mozes = 0
        pocet = random.randint(10, 30)
        for d in range(pocet):
            i = random.randint(1, 6)
            i2 = random.randint(1, 6)
            canvas.itemconfig(self.kocka1, image=self.zozkociek[i - 1])
            canvas.itemconfig(self.kocka2, image=self.zozkociek[i2 - 1])
            canvas.update()
            canvas.after(100)
            self.hod1 = i
            self.hod2 = i2
        Vypis.posud(self)

    def vymaz(self):
        """
        Funkcia vymaze karticku vytvorenu funkciou klik
        """
        for x in self.zoz:
            canvas.delete(x)
        self.buttx.place_forget()

    def kto_ide(self, hrac):
        """
        vytvori ikonku podla kto je na tahu
        """
        if self.ktoide is not None:
            canvas.delete(self.ktoide)
        if self.hraci[hrac]["postavicka"] == "auto":
            self.autorr = self.auto.resize((100, 100))
            self.autouloz = ImageTk.PhotoImage(self.autorr)
            self.ktoide = canvas.create_image(950, 450, image=self.autouloz)
        elif self.hraci[hrac]["postavicka"] == "bota":
            self.botarr = self.bota.resize((100, 100))
            self.botauloz = ImageTk.PhotoImage(self.botarr)
            self.ktoide = canvas.create_image(950, 450, image=self.botauloz)
        elif self.hraci[hrac]["postavicka"] == "macka":
            self.mackarr = self.macka.resize((100, 100))
            self.mackauloz = ImageTk.PhotoImage(self.mackarr)
            self.ktoide = canvas.create_image(950, 450, image=self.mackauloz)
        elif self.hraci[hrac]["postavicka"] == "lod":
            self.lodrr = self.lod.resize((100, 100))
            self.loduloz = ImageTk.PhotoImage(self.lodrr)
            self.ktoide = canvas.create_image(950, 450, image=self.loduloz)
        elif self.hraci[hrac]["postavicka"] == "furik":
            self.furikrr = self.furik.resize((100, 100))
            self.furikuloz = ImageTk.PhotoImage(self.furikrr)
            self.ktoide = canvas.create_image(950, 450, image=self.furikul)
        elif self.hraci[hrac]["postavicka"] == "klobuk":
            self.klobukre = self.klobuk.resize((100, 100))
            self.klobukuloz = ImageTk.PhotoImage(self.klobukre)
            self.ktoide = canvas.create_image(950, 450, image=self.klobukuloz)

    def posun(self, hrac, x, y):
        """posuva hracov"""
        if self.hraci[hrac]["postavicka"] == "auto":
            canvas.move(self.autopostavicka, x, y)
        elif self.hraci[hrac]["postavicka"] == "bota":
            canvas.move(self.botapostavicka, x, y)
        elif self.hraci[hrac]["postavicka"] == "macka":
            canvas.move(self.mackapostavicka, x, y)
        elif self.hraci[hrac]["postavicka"] == "lod":
            canvas.move(self.lodpostavicka, x, y)
        elif self.hraci[hrac]["postavicka"] == "furik":
            canvas.move(self.furikpostavicka, x, y)
        elif self.hraci[hrac]["postavicka"] == "klobuk":
            canvas.move(self.klobukpostavicka, x, y)



class Vypis(Program):

    def __init__(self):
        """
        zavola parent triedu aby sa nacitala
        a spusti funkciu na klikanie
        aj funkciu ktora vseto otvara
        """

        def zmena_hraca(self, hraci):
            self.hraci = hraci
            print(self.hraci)
            self.hraci["Hrac1"]["Money"] += 50
        self.klik_na_karticku()
        super().__init__()
        self.openit()
        self.kto = 0

    def openit(self):
        """otvori vsetko co treba"""
        self.auto = Image.open(r"Images/auto.png")
        self.bota = Image.open(r"Images/bota.png")
        self.furik = Image.open(r"Images/furik.png")
        self.klobuk = Image.open(r"Images/klobuk.png")
        self.lod = Image.open(r"Images/lod.png")
        self.macka = Image.open(r"Images/macka.png")
        self.dom = Image.open(r"Images/dom.png")
        self.hotel = Image.open(r"Images/hotel.png")
        self.autou = ImageTk.PhotoImage(self.auto)
        self.botau = ImageTk.PhotoImage(self.bota)
        self.mackau = ImageTk.PhotoImage(self.macka)
        self.lodu = ImageTk.PhotoImage(self.lod)
        self.furiku = ImageTk.PhotoImage(self.furik)
        self.klobuku = ImageTk.PhotoImage(self.klobuk)

    def klik_na_karticku(self):
        """
        Funkcia caka na kliknutie na karticku aby ju mohla ukazat
        """
        canvas.bind('<ButtonPress>', super().klik)

    def hra(self):
        """prvotne ukazanie toho kto ide"""
        super().kto_ide(self.zoznamhracov[self.kto])

    def dalsi(self):
        """
        Meni kto ide
        a meni aj ikonku vedla kociek ukatujucu kto ide
        """
        if self.kto == self.pocethracov - 1:
            self.kto = 0
        else:
            self.kto += 1

        self.mozes = 1
        self.kto_ide(self.zoznamhracov[self.kto])

    def posud(self):
        """
        Zisti aky hrac je na tahu spocita kolko hodil
        a vypocita jeho posun podla toho kde ma pred posunom figurku
        """
        c = self.hod1 + self.hod2
        if self.hraci[self.zoznamhracov[self.kto]]["postavicka"] == "auto":
            x, y = canvas.coords(self.autopostavicka)
        elif self.hraci[self.zoznamhracov[self.kto]]["postavicka"] == "bota":
            x, y = canvas.coords(self.botapostavicka)
        elif self.hraci[self.zoznamhracov[self.kto]]["postavicka"] == "macka":
            x, y = canvas.coords(self.mackapostavicka)
        elif self.hraci[self.zoznamhracov[self.kto]]["postavicka"] == "lod":
            x, y = canvas.coords(self.lodpostavicka)
        elif self.hraci[self.zoznamhracov[self.kto]]["postavicka"] == "furik":
            x, y = canvas.coords(self.furikpostavicka)
        elif self.hraci[self.zoznamhracov[self.kto]]["postavicka"] == "klobuk":
            x, y = canvas.coords(self.klobukpostavicka)
        if 40 <= x <= 800 and 720 <= y <= 780:
            if x - c * 66 <= 66:
                d = (x - 44) // 66
                super().posun(self.zoznamhracov[self.kto], d * -66, 0)
                super().posun(self.zoznamhracov[self.kto], 0, (c - d) * -66, )
            else:
                super().posun(self.zoznamhracov[self.kto], c * -66, 0)
        elif 40 <= x <= 100 and 40 <= y <= 720:
            if y - c * 66 <= 40:
                d = (y-44) // 66
                super().posun(self.zoznamhracov[self.kto],0, d * -66)
                super().posun(self.zoznamhracov[self.kto],  (c - d) * 66,0)
            else:
                super().posun(self.zoznamhracov[self.kto], 0, -c * 66)
        elif 40< x < 760 and 40<y<100:
            if x +c *66 >800:
                d = (780-x) // 66
                super().posun(self.zoznamhracov[self.kto],  d * 66,0)
                super().posun(self.zoznamhracov[self.kto], 0,(c - d) * 66)
            else:
                super().posun(self.zoznamhracov[self.kto], c * 66, 0)
        elif 40<x<800 and 20<y<780:
            if y + c*66 > 800:
                d = (780-y) // 66
                super().posun(self.zoznamhracov[self.kto],0, d * 66)
                super().posun(self.zoznamhracov[self.kto],  (c - d) * -66,0)
            else:
                super().posun(self.zoznamhracov[self.kto], 0, c * 66)


        self.dalsi()

root = tkinter.Tk()
root.attributes('-fullscreen', True)  # make main window full-screen
canvas = tkinter.Canvas(root)
canvas.pack(fill=tkinter.BOTH, expand=True, )
x = Vypis()

canvas.mainloop()
