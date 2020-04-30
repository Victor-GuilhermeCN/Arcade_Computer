from random import randint
from Functions import line, title, instructions

player_points = []
machine_points = []

def contin():
    ans = str(input('Do you want to continue: [Y/N]:')).upper().strip()[0]
    while ans not in 'YN':
        print('Enter only Y or N!')
        line()
        ans = str(input('Do you want to continue: [Y/N]: ')).upper().strip()[0]
    if ans == 'Y':
        return verify_numb()
    else:
        while True:
            line()
            print('See you soon!')
            break



def verify_numb():
    title('JO-KEN-PÔ')
    instructions('Hello, choose between Scissors, Paper or Rock.\n'
                 '[0] - Scissors\n'
                 '[1] - Paper\n'
                 '[2] - Rock')
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
        machine = randint(0, 2)
        # Getting names to sort machine numbers
        if machine == 0:
            name_machine = 'Scissors'
        elif machine == 1:
            name_machine = 'Paper'
        else:
            name_machine = 'Rock'

        if player == 0:
            player_choice = 'Scissors'
        elif player == 1:
            player_choice = 'Paper'
        else:
            player_choice = 'Rock'

        # Checking the results to get a winner.
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
            player_points.append(1)
            print(f'Machine: {name_machine} X Player: {player_choice}\n'
                  f'You win!\n'
                  f'Machine Points: {sum(machine_points)} x Player Points: {sum(player_points)}')
            return line(), contin()
        elif player == 1 and machine == 2:
            player_points.append(1)
            print(f'Machine: {name_machine} X Player: {player_choice}\n'
                  f'You win!\n'
                  f'Machine Points: {sum(machine_points)} x Player Points: {sum(player_points)}')
            return line(), contin()
        elif player == 2 and machine == 0:
            player_points.append(1)
            print(f'Machine: {name_machine} X Player: {player_choice}\n'
                  f'You win!\n'
                  f'Machine Points: {sum(machine_points)} x Player Points: {sum(player_points)}')
            return line(), contin()
        else:
            machine_points.append(1)
            print(f'Machine: {name_machine} X Player: {player_choice}\n'
                  f'Machine win!\n'
                  f'Machine Points: {sum(machine_points)} x Player Points: {sum(player_points)}')
            return line(), contin()

verify_numb()