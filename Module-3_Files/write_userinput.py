fl=open('test.txt','a')

stid=input("Enter your ID:")
stnm=input("Enter your Name:")

fl.write(f"ID={stid}\nName={stnm}\n")