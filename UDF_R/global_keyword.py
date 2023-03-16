a=34

print("A is:",a)

def getval():
    global a
    a=90
    print("A is:",a)

getval()