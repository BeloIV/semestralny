import tkinter

def start():
    canvas.coords(auto1, 0, 150)
    canvas.coords(auto2, 600, 150)
    pohyb()

def pohyb():
    canvas.move(auto1, 4, 0)
    canvas.move(auto2, -5, 0)
    x_auto1 = canvas.coords(auto1)[0]
    x_auto2 = canvas.coords(auto2)[0]
    if x_auto1 > x_auto2 - 140:
        canvas.create_text(200, 50, text='BUM', fill='red', font='arial 40 bold')
    else:
        canvas.after(30, pohyb)

canvas = tkinter.Canvas(width=800,height=900)
canvas.pack()

obr_auto1 = tkinter.PhotoImage(file='auto1.png')
obr_auto2 = tkinter.PhotoImage(file='auto2.png')

auto1 = canvas.create_image(0, 150, image=obr_auto1)
auto2 = canvas.create_image(600, 150, image=obr_auto2)

tkinter.Button(text='Štart', command=start).pack()
start()
pohyb()


tkinter.mainloop()