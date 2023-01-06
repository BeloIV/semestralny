import tkinter as tk

class PersonInfo:
    def __init__(self, root):
        self.root = root
        self.root.state("zoomed")  # make the window full screen

        # create a canvas that fills the entire window
        self.canvas = tk.Canvas(root, width=root.winfo_screenwidth(), height=root.winfo_screenheight())
        self.canvas.pack()

        self.display_person_info()

    def display_person_info(self):
        # draw a rectangle on the canvas
        self.canvas.create_rectangle(25, 25, 400, 100, fill="light blue")

        # display some text on the canvas
        self.canvas.create_text(150,50, text="John Smith\nAge: 30\nOccupation: Software Developer", fill="black", font=("Arial", ))

root = tk.Tk()
PersonInfo(root)
root.mainloop()