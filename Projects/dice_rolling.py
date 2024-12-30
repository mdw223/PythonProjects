from random import randint

def play():
    dice_1 = randint(0,6)
    dice_2 = randint(0,6)
    print(f'({str(dice_1)}, {str(dice_2)})\n')

loop = True
while loop:
    user = input("Roll dice? (y/n): ")

    if user == 'n':
        loop = False
    elif user == 'y':
        play()
