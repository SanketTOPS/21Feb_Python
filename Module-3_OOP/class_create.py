class studinfo:
    stid=12
    stnm="Sanket"

    def getdata(self):
        print("This is a class.")


# Object of class
st=studinfo()
print(st.stid)
print(st.stnm)
st.getdata()