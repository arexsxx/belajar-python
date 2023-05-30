class persegipanjang:
    def __init__(self, p=0.0,l=0.0):
        self.panjang=p
        self.lebar=l
    def luas(self):
        return self.panjang*self.lebar
    def keliling(self):
        return 2*(self.panjang+self.lebar)    


