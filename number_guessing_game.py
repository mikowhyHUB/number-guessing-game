

from curses.ascii import isdigit
from random import randint

# zacznij jakim numberem chce user mieć maks range w grze
maks_numb = int(input('What number would like to pick to be maks number: '))

# niech komputer wybierze randomowa liczbe za pomoca randomint(0, wybor usera)
random_numb = randint(1, maks_numb)
# zabezpiecz odpowiedź od stringow(isdigit) i liczb ponizej zera. Jezeli sie nie zgadza to quit

while True:
    guess = int(input('Pick a number: '))
    if guess == random_numb:
        print('Congratz, you got it!')
        quit()
    elif guess < 1:
        print('only numbers above 1')
        print('wrong number')


# uyj while true by user zgadywal numer jaki komputer wylosowal
# podlicz ile razy ktos probowal razy zgadanac number
# mozna ulepszyc gre za pomocą dodania ifelse który wskaze czy nie przeskoczylismy numeru
