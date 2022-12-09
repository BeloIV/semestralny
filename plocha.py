import tkinter
from tkinter import ttk
import json


karticky = json.load(open('subor.txt'))


class Program:
    def __init__(self):
        canvas.create_rectangle(110, 110, 704, 704, )
        self.x = 10
        self.y = 110
        canvas.create_rectangle(10, 10, 804, 804)
        canvas.update()
        canvas.after(10)
        canvas.create_rectangle(self.x, self.y, self.x + 100, self.y)
        pocitac=0
        kam=1
        postupnost=karticky["postuponost"]
        print(postupnost)
        for i in karticky["postuponost"]:

            print(i)
            if kam == 1:
                angl= -90
                anlx= 10
                angly= 33
                plusx=100
                plusy=66
                plusnafarbux = 66
                plusnafarbuy = 0
                posunx = 0
                posuny = 66
                zatackax=100
                zatackay = 0
                farbax = 100
                farbay = 66
            if kam == 2:
                angl= 0
                anlx = 33
                angly = 90
                plusx = 66
                plusy = 100
                plusnafarbux = 0
                plusnafarbuy = 34
                farbax=66
                farbay=0
                posunx = 66
                posuny = 0
            elif kam == 3:
                angl=90
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
            elif kam == 4:
                angl=0
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
            canvas.create_rectangle(self.x, self.y, self.x + plusx, self.y + plusy)
            canvas.update()
            canvas.after(100)
            karticky[i]["indexod"] = self.x
            karticky[i]["indexdo"] = self.x + plusx
            karticky[i]["indexyod"] = self.y
            karticky[i]["indexydo"] = self.y + plusy
            if karticky[i]["Nakupna cena"] is not None:
                canvas.create_text(self.x + anlx, self.y + angly,text=(str(karticky[i]["Nakupna cena"])+"$") ,anchor="center", angle=angl)
            if karticky[i]["Farba"] is not None:
                canvas.create_rectangle(self.x + plusnafarbux, self.y+ plusnafarbuy, self.x + farbax, self.y + farbay, fill=karticky[i]["Farba"])
            if pocitac == 8:
                self.y += posuny + zatackay
                self.x += zatackax + posunx
                pocitac = 0
                kam += 1
            else:
                self.y += posuny
                self.x += posunx
                pocitac += 1
        with open('subor.txt', 'w') as subor:
            json.dump(karticky, subor, indent=4)


root = tkinter.Tk()
root.attributes('-fullscreen', True)  # make main window full-screen
canvas = tkinter.Canvas(root)
canvas.pack(fill=tkinter.BOTH, expand=True, )
x = Program()

canvas.mainloop()


