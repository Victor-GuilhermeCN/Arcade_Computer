from random import randint

def line():
    print('-' * 70)

def contin():
    ans = str(input('Do you want to continue: [Y/N]:')).upper().strip()[0]
    while ans not in 'YN':
        print('Enter only Y or N!')
        line()
        ans = str(input('Do you want to continue: [Y/N]: ')).upper().strip()[0]
    if ans == 'Y':
        return line(), verify_numb()
    else:
        while True:
            line()
            print('See you soon!')
            break


machine = randint(0, 2)
name_machine = ''
# Getting names to sort machine numbers
if machine == 0:
    name_machine = 'Scissors'
elif machine == 1:
    name_machine = 'Paper'
else:
    name_machine = 'Rock'


def verify_numb():
    try:
        player = int(input('Enter your number: '))
        # Checking if the data entered are numbers.
        if type(player) != int or player > 3:
            print('Enter only the chosen number!')
            return line(), verify_numb()
    except:
        print('Enter only the chosen number! ')
        return line(), verify_numb()
    else:
        if player == 0:
            player_choice = 'Scissors'
        elif player == 1:
            player_choice = 'Paper'
        else:
            player_choice = 'Rock'

        if player == 0 and machine == 0:
            print(f'Machine: {name_machine} X Player: {player_choice}\n'
                  f'Tie in the game!')
            return line(), contin()
        elif player == 1 and machine == 1:
            print(f'Machine: {name_machine} X Player: {player_choice}\n'
                  f'Tie in the game!')
            return line(), contin()
        elif player == 2 and machine == 2:
            print(f'Machine: {name_machine} X Player: {player_choice}\n'
                  f'Tie in the game!')
            return line(), contin()
        elif player == 0 and machine == 1:
            print(f'Machine: {name_machine} X Player: {player_choice}\n'
                  f'You win!')
            return line(), contin()
        elif player == 1 and machine == 2:
            print(f'Machine: {name_machine} X Player: {player_choice}\n'
                  f'You win!')
            return line(), contin()
        elif player == 2 and machine == 0:
            print(f'Machine: {name_machine} X Player: {player_choice}\n'
                  f'You win!')
            return line(), contin()
        else:
            print(f'Machine: {name_machine} X Player: {player_choice}\n'
                  f'Machine win!')
            return line(), contin()
