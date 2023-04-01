class screen1:
    def getdata(self,id,name):
        print("ID:",id)
        print("Name:",name)

class screen2(screen1):
    def getdata(self, id, name):
        return super().getdata(id, name)

s1=screen1()
s2=screen2()
s1.getdata(1,'Nirav')

s2.getdata(2,'Sanket')