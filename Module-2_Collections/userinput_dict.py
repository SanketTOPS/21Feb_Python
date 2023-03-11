stdata=dict()

n=int(input("Enter number of pairs for dict:"))

for i in range(n):
    key=input("Enter a key:")
    value=input("Enter a value:")
    stdata[key]=value

print(stdata)
