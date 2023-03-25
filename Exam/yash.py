# Get user information and store in file, also read from files same data.
# ID, Name, Subject, City


#f1 = open("new.txt",'x')

f2 = open("new.txt",'a')

def userdata():
    id = input("Enter Student id : ")
    name = str(input("Enter Student name : "))
    subject = str(input("Enter Subject name : "))
    city = str(input("Enter city name : "))

    f2.write(f"id : {id}\n")
    f2.write(f"name : {name}\n")
    f2.write(f"subject : {subject}\n")
    f2.write(f"city : {city}\n")

n = int(input("Enter a number : "))

for i in range(n):
    userdata()



