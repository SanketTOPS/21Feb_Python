import re

email="sanket2020@gmail.com"

email_pattern="^[a-z0-9._]+[@]+[a-z]+[\.]+[a-z]{2,}$"

x=re.findall(email_pattern,email)

if x: #true
    print("Email is valid!")
else:
    print("Error! Invalid email")