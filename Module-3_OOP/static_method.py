class studinfo:
    @staticmethod
    def getdata(id,name):
        print("ID:",id)
        print("Name:",name)


st=studinfo()
id=input("Enter ID:")
nm=input("Enter Name:")
st.getdata(id,nm)