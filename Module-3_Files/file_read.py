fl=open('newfile.txt','r')

#print(fl.read())
#print(fl.readline())
#print(fl.readline(3))
#print(fl.readlines())
#print(fl.readlines()[3])

"""n=1
for i in fl:
    #print(i)
    print(f"Line:{n} = {i}")
    n+=1"""

if fl.readable():
    print("Yes...")
else:
    print("Error!")