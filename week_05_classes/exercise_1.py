#Tinh dien tich va chu vi hinh chu nhat
#PhamNgocCong_24119116
class Hcn:
    def __init__(self,a,b):
        self.chieu_dai=a
        self.chieu_rong=b
    def display(self):
        print(f"Dien tich hcn la: {self.dientich()}, Chu vi hcn la: {self.chuvi()}")
    def dientich(self):
        return self.chieu_dai*self.chieu_rong
    def chuvi(self):
        return (self.chieu_dai+self.chieu_rong)*2
nhap=Hcn(int(input("chieu dai: ")), int(input("Chieu rong: ")))
nhap.display()