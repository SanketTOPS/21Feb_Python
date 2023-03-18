fl=open('hello.txt','w')

#fl.write("Good Afternoon!")

stid=input("Enter your ID:")
stnm=input("Enter your Name:")

#fl.write(stid)
#fl.write(stnm)

"""fl.write(f"ID={stid}\n")
fl.write(f"Name={stnm}")
"""

if fl.writable():
    print("Yes...")
else:
    print("Error!")

fl.write(f"ID={stid}\nName={stnm}")
