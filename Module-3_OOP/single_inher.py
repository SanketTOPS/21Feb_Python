class father:
    bal=0
    car=0

    def getdata(self):
        self.bal=input("Enter Bank balance details:")
        self.car=input("Enter car details:")

class son(father):
    def printdata(self):
        print("Bank Balance:",self.bal)
        print("Car:",self.car)


sn=son()
sn.getdata()
sn.printdata()
