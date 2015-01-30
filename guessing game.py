#Shaf Nasir

import random

number = random.randint(1,100)
name = input("What is you're name? ")
print("Welcome ",name," to the random guessing game, guess a number between 1 and 100 ")
print("")
#While loop to keep game going until the right number is chosen
while True:
    guess = int(input("Guess:"))
    if guess > number:
        print("Too high guess again!")
    elif guess < number:
        print("Too low guess again!")
    elif guess == number:
        print('')
        print("Awesome you guessed the right number!")
        break
print("")    
print("Thank you for playing!") 
        
