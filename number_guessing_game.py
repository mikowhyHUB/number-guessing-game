'''
do ulepszenia appki:
1. jezeli ponizej 10 to wybrales latwy jezeli powyzej to wybrales sredni itp(linia 17)
2. except value err nie działa. google it
3. 39 i 42 mozna zrobic ladniejszy kod (nie trzeba dwoch elif)
'''
from curses.ascii import isdigit
from random import randint

# first user needs to pick how hard game would it be by chosing maks range number
while True:
    try:
        maks_numb = int(
            input('What number would like to pick to be maks number: '))
        break
    except ValueError:
        print('Higher than 0.')
    except:
        print('Type only numbers.')
    finally:
        print('ok, you chose easy mode')


# computer picking random numbr of the users range
random_numb = randint(1, maks_numb)

# while true for mulitply answers
count = 1
while True:
    guess = input('Pick a number: ')
    # protecting program from wrong inputs
    if guess.isdigit():
        guess = int(guess)
    else:
        print('Next time type a number.')

    if guess == random_numb:
        print('Congratz, you got it!')
        break
    elif guess < random_numb:
        print('Too low.')
        count += 1
    else:
        print('Too high.')
        count += 1
# counting how many moves took to find the answer
print('You did it in', count, ' moves!')
