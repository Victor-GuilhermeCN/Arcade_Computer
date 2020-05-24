from Functions import line
from jokenpo import verify_numb
from kick_a_number import kick_a_number, header
from calc import receiving_the_option
from temperatura_converter import option_chosen
from heads_or_tails import wanna_play

def chosen_option():
    try:
        line()
        opt = str(input('Which option: ')).upper().strip()[0]
        while opt not in '123456':
            print(f'Wrong Option, Try again! ')
            return chosen_option()
    except:
        return f'Wrong Option. Try again!', line(), chosen_option()
    else:
        if opt == '1':
            verify_numb()
        elif opt == '2':
            header()
            kick_a_number()
        elif opt == '3':
            receiving_the_option()
        elif opt == '4':
            option_chosen()
        elif opt == '5':
            wanna_play()
        elif opt == '6':
            while True:
                line()
                print('See you soon!')
                break

