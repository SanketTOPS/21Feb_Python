fl=open('newfile.txt','a')

def getdata():
    stid=input("Enter ID:")
    stnm=input("Enter Name:")
    fl.write(f"ID={stid}\nName={stnm}\n")

n=int(input("Enter number of students:"))
for i in range(n):
    getdata()