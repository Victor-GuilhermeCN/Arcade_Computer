from Functions import line, title
from databank import register, login


title('ACCESS PAINEL')
print('[1] - Login\n'
      '[2] - Sign UP\n'
      '[3] - Exit')
line()

def check_registration():
    try:
        user = int(input('Wich option you chosed: '))
        if type(user) != int:
            print('Enter only the chosen number!')
            return line(), check_registration()
    except:
        line()
        print('Enter only the chosen number!')
        return line(), check_registration()
    else:
        if user == 1:
            return login()
        elif user == 2:
            return register()
        elif user == 3:
            while True:
                print('See you soon!')
                line()
                break
