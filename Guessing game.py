import random

number = random.randint(1, 20)

player_name = input("Hello, what's your name? ")
number_of_guesses = 0
print('Okay', player_name, 'I am guessing an integer between 1 and 20:')

while number_of_guesses < 5:
    guess = int(input())
    number_of_guesses += 1
    if guess < number:
        print('Your number is too small')
    if guess > number:
        print('Your number is too big')
    if guess == number:
        break
if guess == number:
    print('You guessed the number in', str(number_of_guesses), 'tries')
else:
    print('You failed to guess the number, the number was', str(number))



