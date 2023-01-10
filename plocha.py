import json
import tkinter

from PIL import Image, ImageTk

karticky = json.load(open('subor.txt'))


class Program:
    def __init__(self):
        """
        Otvori vsetky obrazky postaviciek a spusti vstupne dialogove okno s vyberom moznosti hry.
        """
        self.dom = Image.open(r"Images/dom.png")
        self.hotel = Image.open(r"Images/hotel.png")
        self.ximg = tkinter.PhotoImage(file=r"Images/close2.png")
        self.elektrorr = Image.open(r"Images/elektro2.png")
        self.vlak = Image.open(r"Images/vlak2.png")
        self.kohutik = Image.open(r"Images/kohutik2.png")
        self.dan = Image.open(r"Images/dan2.png")

        self.ram = None

        self.karticky = json.load(open('subor.txt'))
        vezenie = Image.open(r"Images/vezenie.jpg")
        self.vezenie = ImageTk.PhotoImage(vezenie)
        policajt = Image.open(r"Images/policajt.png")
        policajt = policajt.rotate(-45)
        self.policajt = ImageTk.PhotoImage(policajt)
        wifi = Image.open(r"Images/wifi.png")

        wifi = wifi.rotate(45)
        self.wifi = ImageTk.PhotoImage(wifi)

        """Spusti Vykreslovanie hriacej plochy."""
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
            if self.karticky[i]["Farba"] is not None:
                canvas.create_rectangle(self.x + plusnafarbux, self.y + plusnafarbuy, self.x + farbax, self.y + farbay,
                                        fill=self.karticky[i]["Farba"])
            if self.karticky[i]["Nakupna cena"] is not None:
                canvas.create_text(self.x + anlx, self.y + angly, text=(str(self.karticky[i]["Nakupna cena"]) + "$"),
                                   anchor="center", angle=angl)
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
        self.klik_na_karticku()

    def klik_na_karticku(self):
        canvas.bind('<ButtonPress>', self.klik)
    def vymaz(self):

        for x in self.zoz:
            canvas.delete(x)
        self.buttx.place_forget()
    def klik(self, event):

        # if 580 < event.x < 600 and 200 < event.y < 220:
        # canvas.delete(self.ram, self.text, self.buttx, self.texxx,self.textnajom,self.podklad)
        # self.ram = None

        if self.ram is not None:

            for x in self.zoz:
                canvas.delete(x)
            self.buttx.place_forget()
            karta = None
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

        if karta is not None and "Sanca" not in karta and "Pokladna" not in karta :



            if "Energeticke zavody" in karta or "Vodarne" in karta:

                self.ram = canvas.create_rectangle(270, 220, 530, 580, fill="white")
                self.text = canvas.create_text(400, 240, text=self.karticky[karta]["Nazov"], fill="black",
                                               font="Arial 25")
                kk= self.karticky[karta]["popis"].split()

                if "Energeticke zavody" in karta:
                    self.elektror = self.elektrorr.resize((200,200))
                    self.elektrouloz = ImageTk.PhotoImage(self.elektror)
                    self.obrazok = canvas.create_image(400,400,image=self.elektrouloz)


                else:
                    self.kohutikr = self.kohutik.resize((200,200))
                    self.kohutikuloz = ImageTk.PhotoImage(self.kohutikr)
                    self.obrazok = canvas.create_image(400,400,image=self.kohutikuloz)


                pocitadlo = 0
                vypis = ""
                for slovo in kk:
                    if "Ak" in slovo:
                        vypis += "\n" + slovo + " "
                        pocitadlo = 0
                    elif pocitadlo < 20:
                        vypis+= slovo + " "
                        pocitadlo += len(slovo) +1
                    else:
                        vypis += "\n" + slovo + " "
                        pocitadlo =0
                vypis = vypis.strip()
                self.popis = canvas.create_text(400, 350, text=vypis, fill="black", font="Helvetica 15")
                self.texthypoteka = canvas.create_text(400, 515, text=f'Hypotéka {self.karticky[karta]["Hypoteka"]} $', fill="black", font="Helvetica 18")
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
                self.zoz = [self.ram,self.text,self.vlakra,self.textnajom,self.stan4,self.stan3,self.stan2,self.texthypoteka]
            elif "Dan" in karta:
                self.ram = canvas.create_rectangle(270, 220, 530, 580, fill="white")
                self.text = canvas.create_text(400, 240, text=self.karticky[karta]["Nazov"], fill="black",
                                               font="Arial 25")
                self.danouloz = ImageTk.PhotoImage(self.dan)
                self.danu = canvas.create_image(400, 400, image=self.danouloz)
                self.zaplat = canvas.create_text(400,500,text=f'Zaplať {self.karticky[karta]["Zakladne najomne"]} $' ,fill="black",
                                               font="Arial 25")
                self.zoz = [self.ram,self.text,self.danu,self.zaplat]
            elif "Sanca" not in karta and "zeleznica" not in karta and "Energeticke zavody" not in karta and "Vodarne" not in karta:
                self.ram = canvas.create_rectangle(270, 220, 530, 580, fill=self.karticky[karta]["Farba"])
                self.podklad = canvas.create_rectangle(300, 260, 500, 540, fill="white")
                najomne = f'Nájom {str(self.karticky[karta]["Zakladne najomne"])} $'
                self.textnajom = canvas.create_text(400, 280, text=najomne, fill="black", font="Helvetica 20")
                self.textnajompozn = canvas.create_text(400, 305, text="Nájom sa zdvojnasobuje ak vlastníte\n        všetky budovy z tejto farby.", fill="grey", font="Helvetica 12")
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
                self.textnajom1d = canvas.create_text((490-(len(str(self.karticky[karta]["1 dom"]))*3)), 355,text=f'{str(self.karticky[karta]["1 dom"])} $',fill="black", font="Arial 15")

                self.textnajom2d = canvas.create_text((490-(len(str(self.karticky[karta]["2 domy"]))*3)), 385, text=f'{str(self.karticky[karta]["2 domy"])} $',
                                                      fill="black", font="Arial 15")
                self.textnajom3d = canvas.create_text((490-(len(str(self.karticky[karta]["3 domy"]))*3)), 415, text=f'{str(self.karticky[karta]["3 domy"])} $',
                                                      fill="black", font="Arial 15")
                self.textnajom4d = canvas.create_text((490-(len(str(self.karticky[karta]["4 domy "]))*3)), 445, text=f'{str(self.karticky[karta]["4 domy "])} $',
                                                      fill="black", font="Arial 15")
                self.textnajomhotel = canvas.create_text((490 - (len(str(self.karticky[karta]["4 domy "])) * 3)), 475,
                                                      text=f'{str(self.karticky[karta]["4 domy "])} $',
                                                      fill="black", font="Arial 15")
                self.textstavba= canvas.create_text(400, 490, text=f'Stavba {self.karticky[karta]["Cena domu"]} $ každý.', fill="grey", font="Helvetica 15")
                self.texthypoteka = canvas.create_text(400, 515, text=f'Hypotéka {self.karticky[karta]["Hypoteka"]} $', fill="black", font="Helvetica 18")
                self.text = canvas.create_text(400, 240, text=self.karticky[karta]["Nazov"], fill="white",
                                               font="Arial 25")
                self.zoz = [self.ram, self.text, self.textnajom, self.podklad, self.dom1, self.dom2,
                   self.dom3, self.dom4, self.dom5, self.dom6, self.dom7, self.dom8, self.dom9, self.dom10,
                   self.hotel1, self.textnajom1d, self.textnajom2d, self.textnajom3d, self.textnajom4d,
                   self.textnajomhotel,self.texthypoteka,self.textstavba,self.textnajompozn]
            self.buttx = tkinter.Button(text="X",command=self.vymaz, image=self.ximg)
            self.buttx.place(x=350,y=590)

root = tkinter.Tk()
root.attributes('-fullscreen', True)  # make main window full-screen
canvas = tkinter.Canvas(root, background="grey")
canvas.pack(fill=tkinter.BOTH, expand=True, )
x = Program()

canvas.mainloop()
