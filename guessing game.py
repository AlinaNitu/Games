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