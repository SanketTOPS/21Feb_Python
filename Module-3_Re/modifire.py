import re

mystr="This is Python!67768"

#x=re.findall('[A-Z]',mystr)
#x=re.findall('[a-z]',mystr)
#x=re.findall('[A-Za-z]',mystr)
#x=re.findall('[0-9]',mystr)
#x=re.findall('[A-Za-z0-9]',mystr)
#x=re.findall('Py..on',mystr)
#x=re.findall('This|That',mystr)
#x=re.findall('^This',mystr)
#x=re.findall('^[A-Z]',mystr)
x=re.findall('69$',mystr)
print(x)