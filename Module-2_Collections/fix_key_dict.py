stdata=dict()

key=['id','name','sub','city']

n=int(input("Enter number of pairs:"))

if n>len(key):
    print("Error!")
else:
    for i in range(n):
        value=input(f"Enter a value for {key[i]} :")
        stdata[key[i]]=value

    print(stdata)