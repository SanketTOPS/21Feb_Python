id=0
name=""
def getdata():
    id=input("Enter ID:")
    name=input("Enter Name:")
    print("ID:",id)
    print("Name:",name)

n=int(input("Enter number of student:"))

for i in range(n):
    getdata()