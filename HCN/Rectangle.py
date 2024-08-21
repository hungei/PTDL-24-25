class Rectangle:
    def __init__(self,width,lenght):
        self.width=width
        self.lenght=lenght
    def dientich(self):
        dtich=self.width*self.lenght
        return dtich
    def chuvi(self):
        cvi=(self.width+self.lenght)*2
        return cvi
    def hienthi(self):
        print(f"rong:{self.width},dai:{self.lenght},chu vi:{self.chuvi()},dien tich:{self.dientich()}\n")