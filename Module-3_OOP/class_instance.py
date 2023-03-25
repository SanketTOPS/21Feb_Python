class studInfo:
    stid=12
    stnm="Sanket"

    def getdata(self):
        print("ID:",self.stid)
        print("Name:",self.stnm)

# Object of class
"""st=studInfo()
st.getdata()
st.stid=3
st.stnm="Nirav"
st.getdata()"""


# Instance of class
studInfo().getdata()
studInfo().stid=43
studInfo().stnm="Ashok"
studInfo().getdata()