from tkinter import *
from PIL import Image, ImageTk
canvas = Canvas(width=30000, height=20000)
canvas.pack()

images = []  # to hold the newly created image
image = Image.new('RGBA', (10000,10000), (65535, 65535, 65535, 127))
images.append(ImageTk.PhotoImage(image))
canvas.create_image(0, 0, image=images[-1], anchor='nw')






canvas.mainloop()