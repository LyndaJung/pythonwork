
'''
Question 1
Write code that asks the user to input a number between 1 and 5 inclusive.
The code will take the integer value and print out the string value. So for
example if the user inputs 2 the code will print two. Reject any input that
is not a number in that range
'''

user_input = int(input("Enter a number between 1 and 6 inclusive: "))
if user_input == 1:
    print("one")
elif user_input == 2:
    print("two")
elif user_input == 3:
    print("three")
elif user_input == 4:
    print("four")
elif user_input == 5:
    print("five")
elif user_input == 6:
    print("six")
else:
    print("out of range")

#guess secret number

import random

secret_number = random.randint(0,9)
guess = input('Guess the number between 1-10:> ')
if guess.isdigit():
   guess = int(guess)
   if guess == secret_number:
       print('You guessed the correct number! You win!')
   elif guess > secret_number and guess <= 9:
       print('You guessed too high. Sorry you lose!')
   elif guess < secret_number and guess >= 0:
       print('You guessed too low. Sorry you lose!')
   else:
       print('Out of range')
else:
   print('That\'s not even an integer! What are you playing at?!')