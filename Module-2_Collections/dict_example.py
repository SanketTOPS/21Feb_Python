stdata={'id':101,'name':'nirav','sub':'python'}
"""print(stdata)
print(stdata['name'])
print(stdata.get('sub'))
print(len(stdata))"""

"""if 'nirav' in stdata:
    print("Yes...")
else:
    print("Noo")"""

"""if 'nirav' in stdata.values():
    print('Yes...')
else:
    print('Noo')"""

"""print(stdata)
print(stdata.keys())
print(stdata.values())"""

#print(stdata)

"""for i in stdata:
    print(i)"""

"""for i in stdata.values():
    print(i)"""

"""for i in stdata.items():
    print(i)"""

"""stdata['id']=102 #update value

for i,j in stdata.items():
    #print(i,j)
    print(f"Key={i} and Value={j}")"""

stdata['city']='rajkot' #adding items
#stdata.pop('name')
#del stdata['name']
#stdata.clear()
#del stdata
#print(stdata)

newdict=stdata.copy()
print(newdict)