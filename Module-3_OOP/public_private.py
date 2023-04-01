class student:
    __stid=12
    __stnm="Nirav"

    def __getdata(self):
        print("This is getdata.")
        print("ID:",self.__stid)
        print("Name:",self.__stnm)
    
    def getvalue(self):
        self.__getdata()

st=student()
#print(st.stid)
#print(st.stnm)
#st.getdata()
st.getvalue()
