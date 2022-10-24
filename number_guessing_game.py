'''
do ulepszenia appki:
1. jezeli ponizej 10 to wybrales latwy jezeli powyzej to wybrales sredni itp(linia 17)
2. except value err nie działa. google it
3. 39 i 42 mozna zrobic ladniejszy kod (nie trzeba dwoch elif)
'''
from curses.ascii import isdigit
from random import randint

# zacznij jakim numberem chce user mieć maks range w grze i zabezpiecz od złych odp
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


# niech komputer wybierze randomowa liczbe za pomoca randomint(0, wybor usera)
random_numb = randint(1, maks_numb)
# zabezpiecz odpowiedź od stringow(isdigit) i liczb ponizej zera. Jezeli sie nie zgadza to quit
# uyj while true by user zgadywal numer jaki komputer wylosowal
count = 1
while True:
    guess = input('Pick a number: ')
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
# podlicz ile razy ktos probowal razy zgadanac number
print('You did it in', count, ' moves!')


# mozna ulepszyc gre za pomocą dodania ifelse który wskaze czy nie przeskoczylismy numeru
