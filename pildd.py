import random
from PIL import Image, ImageTk
import tkinter

import tkinter

# moduly Image ani ImageTk tu nepotrebujeme

canvas = tkinter.Canvas(width=800, height=800)
canvas.pack()
tk_id = canvas.create_image(200, 150)
tk_id2 = canvas.create_image(200, 200)
zoz = [tkinter.PhotoImage(file=f'Images/dice/roll{i}.png') for i in range(1,7)]
i = 0
i2 = 0
for d in range(30):
    i = random.randint(1, 6)
    i2 = random.randint(1, 6)
    canvas.itemconfig(tk_id, image=zoz[i-1])
    canvas.itemconfig(tk_id2, image=zoz[i2-1])
    canvas.update()
    canvas.after(100)

canvas.mainloop()


