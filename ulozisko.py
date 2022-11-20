"""

        canvas.update()
        canvas.after(10)
        zoz=["orange","orange",None,"orange",None,"deeppink","deeppink",None,"deeppink"]
        for i in zoz:

            canvas.create_rectangle(10, self.y, 110, self.y+ 66)
            if i !=None:
                canvas.create_rectangle(86,self.y,110,self.y+66,fill=i)
            self.y +=66
            canvas.update()
            canvas.after(10)
        canvas.update()
        canvas.after(10)
        canvas.create_rectangle(10,self.y,110,self.y+100)
        self.x +=100
        zoz=["blue","blue",None,"blue",None,None,"brown",None,"brown"]
        for i in zoz:
            canvas.update()
            canvas.after(10)
            canvas.create_rectangle(self.x, self.y, self.x+66, self.y+100)
            if i !=None:
                canvas.create_rectangle(self.x,self.y+20,self.x+66,self.y,fill=i)
            self.x +=66
        canvas.update()
        canvas.after(10)
        canvas.create_rectangle(self.x, self.y, self.x+100, self.y + 100)

    def kresli(self):
    """