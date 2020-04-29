from random import randint
from Functions import line, instructions, title


def sort_side():
    machine = randint(0, 1)
    machine_face_nickel = ''
    if machine == 0:
        machine_face_nickel = 'Heads'
    elif machine == 1:
        machine_face_nickel = "Tails"
    return machine_face_nickel


def contin():
    ans = str(input('Do you want to continue: [Y/N]:')).upper().strip()[0]
    try:
        while ans not in 'YN':
            print('Enter only Y or N!')
            line()
            ans = str(input('Do you want to continue: [Y/N]: ')).upper().strip()[0]
    except:
        return contin()
    else:
        if ans == 'Y':
            return line(), wanna_play()
        else:
            while True:
                line()
                print('See you soon!')
                break


def wanna_play():
    title('HEADS OR TAILS')
    instructions('Welcome to the game Heads or Tails.\n'
                 'We can sort 2 sides of the coin.')
    try:
        player = str(input('Do you want to play Heads or Tails [Y/N]: ')).upper().strip()[0]
        line()
        while player not in 'YN':
            print('Enter only Y or N.')
            return line(), wanna_play()
    except:
        return wanna_play()
    else:
        if player == 'Y':
            print(f'Your side of the coin was {sort_side()}')
            return line(), contin()
        else:
            while True:
                line()
                print('See you soon!')
                break
