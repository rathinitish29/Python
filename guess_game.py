#Number guessing Game

import random
winning_number = random.randint(1,100)
guess = 1
number = int(input('Enter a number between 1 - 100 : '))
game_over = False

while True :
    if number == winning_number :
        print(f'you win , and you guessed this number in {guess} times')
        break
    else:
        if number < winning_number:
            print('too low ')
            guess +=  1
            number = int(input('guess again '))
        else:
            print('too high')
            guess += 1
            number = int(input('guess again '))
            
