# Create a module for signup and login.
n=input('Are you regestered ?(y/n): ')
def data():
    print('enter your information\n')
    input('enter your username: ')
    input('enter password: ')
    print('Thanks for login')

if n=='y':
    data()
else:
    print(input('enter your email-id: '))
    print('you are a verified user\n')
    data()
