from basicoperations import BasicOperations

# Create a line.
def line():
    print('-' * 70)

def title(msg):
    line()
    print(msg.center(70))
    line()

def instructions():
    title('CALCULATOR')
    print('We have the 4 basic operations of mathematics.\n'
          '1 - ADD\n'
          '2 - SUBSTRACT\n'
          '3 - MULTIPLY\n'
          '4 - DIVIDE\n'
          '5 - EXIT')
    line()

def contin():
    ans = str(input('Do you want to continue: [Y/N]:')).upper().strip()[0]
    while ans not in 'YN':
        print('Enter only Y or N!')
        line()
        ans = str(input('Do you want to continue: [Y/N]: ')).upper().strip()[0]
    if ans == 'Y':
        return line(), receiving_the_option()
    else:
        while True:
            line()
            print('See you soon!')
            break


def receiving_the_option():
    instructions()

    try:
        opt = int(input('Which option is chosen: '))
        line()
        if type(opt) != int or opt > 5:
            print('The number is greater than 5.\n'
                  'Try again.')
            return line(), receiving_the_option()
    except:
        print('It is not a number\n'
              'Try again.')
        return line(), receiving_the_option()
    else:
        if opt == 1:
            try:
                value1 = int(input('1º Number: '))
                value2 = int(input('2º Number: '))
                if type(value1) != int:
                    print('It is not a number.a')
                    return line(), receiving_the_option()
            except:
                print('It is not a number.n')
                return line(), receiving_the_option()
            else:
                user = BasicOperations(value1, value2)
                print(f'{value1} + {value2} = {user.add(value1, value2)}')
            return line(), contin()
        elif opt == 2:
            try:
                value1 = int(input('1º Number: '))
                value2 = int(input('2º Number: '))
                if type(value1) != int:
                    print('It is not a number.a')
                    return line(), receiving_the_option()
            except:
                print('It is not a number.n')
                return line(), receiving_the_option()
            else:
                user = BasicOperations(value1, value2)
                print(f'{value1} - {value2} = {user.subtract(value1, value2)}')
            return line(), contin()
        elif opt == 3:
            try:
                value1 = int(input('1º Number: '))
                value2 = int(input('2º Number: '))
                if type(value1) != int:
                    print('It is not a number.a')
                    return line(), receiving_the_option()
            except:
                print('It is not a number.n')
                return line(), receiving_the_option()
            else:
                user = BasicOperations(value1, value2)
                print(f'{value1} X {value2} = {user.mult(value1, value2)}')
            return line(), contin()
        elif opt == 4:
            try:
                value1 = int(input('1º Number: '))
                value2 = int(input('2º Number: '))
                if type(value1) != int:
                    print('It is not a number.a')
                    return line(), receiving_the_option()
            except:
                print('It is not a number.n')
                return line(), receiving_the_option()
            else:
                user = BasicOperations(value1, value2)
                print(f'{value1} / {value2} = {user.div(value1, value2)}')
            return line(), contin()
        elif opt == 5:
            while True:
                print('See you soon!')
                break

