import tkinter
from tkinter import ttk
import json
from PIL import Image, ImageTk

karticky = json.load(open('subor.txt'))


class Program:
    def __init__(self):
        """
        Otvori vsetky obrazky postaviciek a spusti vstupne dialogove okno s vyberom moznosti hry.
        """
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
                zeleznicax= 60
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
                if self.karticky[i]["Image"] is not None :

                    if i == "zeleznica":
                        print(type(self.zeleznica1),"zeleznica2")
                        if kam == 1:
                            canvas.create_image(self.x + zeleznicax, self.y+zeleznicay, image=self.zeleznica1)
                        elif kam == 2 or kam == 4:
                            canvas.create_image(self.x + zeleznicax, self.y+zeleznicay, image=self.zeleznica2)
                        elif kam == 3:
                            canvas.create_image(self.x + zeleznicax, self.y+zeleznicay, image=self.zeleznica3)
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
                            canvas.create_image(self.x + 50, self.y+33, image=self.elektro1)
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
                            canvas.create_image(self.x , self.y, image=self.voda1)
                        elif kam == 2 or kam == 4:
                            canvas.create_image(self.x -33, self.y -50, image=self.voda2)
                        elif kam == 3:
                            canvas.create_image(self.x, self.y, image=self.voda3)
            except:
                pass

            if "Dan" in i:
                if kam ==2:
                    canvas.create_text(self.x + anlx, self.y + angly-40, text=f'Daň z\nprímu\nzaplaťe:\n{self.karticky[i]["Zakladne najomne"]} $',angle=angl,
                                   anchor="center", font="Ariel 15")
                elif kam ==3:
                    canvas.create_text(self.x + anlx -40, self.y + angly, text=f'Daň z\nprímu\nzaplaťe:\n{self.karticky[i]["Zakladne najomne"]} $',angle=angl,
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


root = tkinter.Tk()
root.attributes('-fullscreen', True)  # make main window full-screen
canvas = tkinter.Canvas(root, background="grey")
canvas.pack(fill=tkinter.BOTH, expand=True, )
x = Program()

canvas.mainloop()
