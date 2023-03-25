class studInfo:
    stid=0
    stnm=""

    def getdata(self):
        self.stid=input("Enter your ID:")
        self.stnm=input("Enter your Name:")
    
    def printdata(self):
        print("Student ID:",self.stid)
        print("Student Name:",self.stnm)

st=studInfo()
st.getdata()
st.printdata()