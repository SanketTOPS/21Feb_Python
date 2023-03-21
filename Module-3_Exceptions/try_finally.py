try:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    print("Sum:",a+b)
except Exception as e:
    print(e)
#finally:
else:
    print("This is Finally block.")