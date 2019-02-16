Assignment:
    Let's use while loops to create a guessing game.

The Challenge:

Write a program that picks a random integer from 1 to 100, and has players guess the number. The rules are:

If a player's guess is less than 1 or greater than 100, say "OUT OF BOUNDS"
On a player's first turn, if their guess is
within 10 of the number, return "WARM!"
further than 10 away from the number, return "COLD!"
On all subsequent turns, if a guess is
closer to the number than the previous guess return "WARMER!"
farther from the number than the previous guess, return "COLDER!"
When the player's guess equals the number, tell them they've guessed correctly and how many guesses it took!

from random import randint

number= randint(1,100)
print(number)

guesses=[]

while True:
    guess = int(input('Pick up a number: '))
    guesses.append(guess)
    print(len(guesses))
    if guess==number:
        print('Congrats, you guesses it in {0} tries and the numbers you tried were: {1}'.format(len(guesses),guesses))
        break
    if guess < 1 or guess >100:
        print('OUT OF BOUND! Please try again:')
        continue
    if len(guesses)>=2 and abs(number-guesses[-2]) > abs(number-guesses[-1]):
        print('WARMER')
        continue
    if len(guesses)>=2 and abs(number-guesses[-2]) < abs(number-guesses[-1]):
        print('COLDER')
        continue
    if abs(number-guess) <=10:
        print('WARM')
        continue
    if abs(number-guess) > 10:
        print('COLD')
        continue
