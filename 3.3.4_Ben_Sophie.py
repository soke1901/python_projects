from __future__ import print_function  # must be first in file


def f(n):
    if int(n) == n:
        if n % 2 == 0:
            if n % 3 == 0:
                print('The number is a multiple of 6.')
            else:
                print('The number is even')
        else:
            print('The number is odd')
    else:
        print('The number is not an integer')


def guess_once():
    secret = 1
    print('I have a number between 1 and 4 inclusive.')
    guess = int(input('Guess: '))
    if guess < secret:
        print('Too low - my number was', secret, '!')
    elif guess > secret:
        print('Too high, my number was', secret, '!')
    else:
        print('Right on! I was number 1!')


def quiz_decimal(low, high):
    number = input("give a number between " + low + "and " + high + ":")
    if number < low:
        print("No, " + number + " is lower than " + low)
    elif number > high:
        print("No, " + number + " is higher than " + high)
    else:
        print("Good! " + low + " < " + number + " < " + high)


quiz_decimal(1, 5)
