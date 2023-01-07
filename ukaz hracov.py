import tkinter
from PIL import Image, ImageTk
import json


class Program:
    def __init__(self):
        self.pocethracov = 3
        self.hraci = {"Hrac1": {"meno": "Hrac 1", "postavicka": "", "karticky": [], "Money": 5000},
                      "Hrac2": {"meno": "Hrac 2", "postavicka": "", "karticky": [], "Money": 5000},
                      "Hrac3": {"meno": "Hrac 3", "postavicka": "", "karticky": [], "Money": 5000},
                      "Hrac4": {"meno": "Hrac 4", "postavicka": "", "karticky": [], "Money": 5000},
                      "Hrac5": {"meno": "Hrac 5", "postavicka": "", "karticky": [], "Money": 5000},
                      "Hrac6": {"meno": "Hrac 6", "postavicka": "", "karticky": [], "Money": 5000}, }
        self.ukaz_hracov()

    def ukaz_hracov(self):
        """Ukaže mena a hodnotu majetku hračov """
        print("hi")
        for x, i in enumerate(self.hraci):
            print(x, i)
            images = []  # to hold the newly created image
            image = Image.new('RGBA', (10000, 10000), (65535, 65535, 65535, 127))
            images.append(ImageTk.PhotoImage(image))
            ramram=canvas.create_image(0, 0, image=images[-1], anchor='nw')
            ram = canvas.create_rectangle(300, 300, 450, 450, fill="light blue")
            text = canvas.create_text(375, 350, text=self.hraci[i]["meno"], fill="black", font="Arial 20")
            text1 = canvas.create_text(375, 370, text=f'Majetok: {self.hraci[i]["Money"]}', fill="black",
                                       font="Arial 15")

            canvas.update()
            canvas.after(1000)
            canvas.delete(ram, text, text1)
            if x == self.pocethracov - 1:
                canvas.delete(ram,ramram)

                break


root = tkinter.Tk()
root.attributes('-fullscreen', True)  # make main window full-screen
canvas = tkinter.Canvas(root)
canvas.pack(fill=tkinter.BOTH, expand=True, )
x = Program()
canvas.mainloop()

