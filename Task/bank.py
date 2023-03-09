ano=input("Enter A/c number:")
anm=input("Enter A/c Name:")
atype=input("Enter A/c Type:")

if atype=='saving' or atype=='current':
    depo=int(input("Enter Deposite amount:"))

    wit=int(input("Enter your withdrwan amount: "))

    if wit>depo:
        print("Error!Plz add more fund in your account.")
    else:
        print("A/c No:",ano)
        print("A/c Name:",anm)
        print("A/c Type:",atype)
        print("Balance:",depo)
        print("Current Balance:",depo-wit)
        

