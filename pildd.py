class A:
    def __init__(self):
        self.x = 4
        self.y = 6
        self.prinnt()

    def prinnt(self):
        print(self.x,self.y)

    def plus(self,x):
        x += 1
        return x

class B (A):
    def __init__(self):
        self.x=5
    def bp(self):
        print(self.x)

class C(A):
    def __init__(self):
        self.x = 9
        super().__init__()

        print(self.x)
        self.repp()
    def cp(self):
        print(self.x)


    def repp(self):

        for i in range(10):
            self.x = super().plus(self.x)
            print(self.x)

x = C()