from time import sleep
def line():
    print('-' * 70)

def title(msg):
    line()
    print(msg.center(70))
    line()

def menu():
    title('TEMPERATURE CONVERTER')
    print(f'Welcome, here you can convert Cº to Fº or Fº to Cº.\n'
          f'[1] - Convert Cº to Fº\n'
          f'[2] - Convert Fº to Cº\n'
          f'[3] - Exit')
    line()
    option_chosen()

def contin():
    ans = str(input('Do you want to continue: [Y/N]:')).upper().strip()[0]
    while ans not in 'YN':
        print('Enter only Y or N!')
        line()
        ans = str(input('Do you want to continue: [Y/N]: ')).upper().strip()[0]
    if ans == 'Y':
        return line(), menu()
    else:
        while True:
            line()
            print('See you soon!')
            break

def option_chosen():
    try:
        opt = int(input('Which option: '))
        if type(opt) != int:
            print('It is not a numnber.')
            return line(), option_chosen()
    except:
        print('It is not a number.')
        return line(), option_chosen()
    else:
        if opt == 1:
            convert_celsius_to_faren()
        elif opt == 2:
            convert_faren_to_celsius()
        elif opt == 3:
            while True:
                print('See you soon!')
                break

def convert_celsius_to_faren():
    try:
        num = int(input('Insert temperature on Cº: '))
        if type(num) != int:
            print('It is not a number.\n')
            return line(), convert_celsius_to_faren()
    except:
        print('It is not a number.')
        return line(), convert_celsius_to_faren()
    else:
        celsius_to_faren = (num * 9/5) + 32
        print('Wait, we are converting...')
        sleep(1)
        for i in range(0, 3):
            print('Converting...')
            sleep(1)
        print(f'You convert {num}Cª to {celsius_to_faren:.2f}ºF')
        return line(), contin()

def convert_faren_to_celsius():
    try:
        num = int(input('Insert a temperature on Fª: '))
        if type(num) != int:
            print('It is not a number.\n')
            return line(), convert_faren_to_celsius()
    except:
        print('It is not a number.\n')
        return line(), convert_faren_to_celsius()
    else:
        faren_to_celsius = (num - 32) * 5 / 9
        print('Wait we are converting...')
        sleep(1)
        for i in range(0, 3):
            print('Converting...')
            sleep(1)
        print(f'You convert {num}Fº to {faren_to_celsius}Cº')
        return line(), contin()
