from jokenpo import verify_numb
from kick_a_number import kick_a_number
from calc import receiving_the_option
from temperatura_converter import option_chosen
from heads_or_tails import wanna_play
def line():
    print('-' * 70)

def title(msg):
    line()
    print(msg.center(70))
    line()

def instructions(msg):
    print(msg)
    line()

def menu_game():
    print('1 - Jokenpô\n'
          '2 - Guess the number\n'
          '3 - Calculator\n'
          '4 - Temperature converter\n'
          '5 - Heads or tails\n'
          '6 - Exit')

def chosen_option():
    line()
    opt = str(input('Which option: ')).upper().strip()[0]
    try:
        while opt not in '123456':
            print(f'Wrong Option')
            return chosen_option()
    except:
        return f'Wrong Option. Try again: ', line(), chosen_option()
    else:
        if opt == '1':
            title('JO-KEN-PO')
            instructions('Play along with machine and choose rock paper and scissors!\n'
                         '[0] - Scissors\n'  
                         '[1] - Paper\n'
                         '[2] - Rock')
            verify_numb()

        elif opt == '2':
            title('Guess the number')
            instructions('The machine will draw a number between 1 and 10, try to guess!')
            kick_a_number()
        elif opt == '3':
            receiving_the_option()
        elif opt == '4':
            title('TEMPERATURE CONVERSER')
            instructions(f'Welcome, here you can convert Cº to Fº or Fº to Cº.\n'
                         f'[1] - Convert Cº to Fº\n'
                         f'[2] - Convert Fº to Cº\n'
                         f'[3] - Exit')
            line()
            option_chosen()
        elif opt == '5':
            title('HEADS OR TAILS')
            wanna_play()
        elif opt == '6':
            while True:
                line()
                print('See you soon!')
                break
