# Create a line.
def line():
    print('-' * 70)

def contin():
    ans = str(input('Do you want to continue: [Y/N]:')).upper().strip()[0]
    while ans not in 'YN':
        print('Enter only Y or N!')
        line()
        ans = str(input('Do you want to continue: [Y/N]: ')).upper().strip()[0]
    if ans == 'Y':
        return line(), kick_a_number()
    else:
        while True:
            line()
            print('See you soon!')
            break

# Checks the value entered by the user.
def kick_a_number():
    from random import randint
    machine = randint(0, 10)
    try:
        number_user = int(input('Kick a number between 0 - 10: '))
        if type(number_user) != int or number_user > 10:
            print('The number is not between 0 - 10, try again.')
            return line(), kick_a_number()
    except:
        print('That is not a number, try again.')
        return line(), kick_a_number()
    else:
        line()
        while True:
            if number_user < machine:
                print('You kicked wrong. The number machine is higher!\n'
                      'Try again. ')
                line()
                return kick_a_number()
                line()
            elif number_user > machine:
                print('You kicked wrong. The number machine is less!\n'
                      'Try again.  ')
                line()
                return kick_a_number()
                line()
            elif number_user == machine:
                print(f'Correct, the number of the machine was {machine}.')
                return line(), contin()
                break
