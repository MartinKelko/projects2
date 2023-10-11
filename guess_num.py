from random import randint

def najdi_cislo():
    #number_definition
    number_definition = randint(0,99)

    #guess_definition
    guess_definition = int(input('Enter a guess: '))

    print('I am thinking of a number between 0 and 99...')
    print('Enter a guess:', str(guess_definition))

    #opakuje sa pokial nesplna podmienku
    while guess_definition != number_definition:
        if guess_definition > number_definition:
            print('your guess is too high')
        else:
            print('your guess is too low')
    #ak uhadne cislo        
        guess_definition = int(input('Enter a guess: '))
    print('Congrats')

najdi_cislo()
