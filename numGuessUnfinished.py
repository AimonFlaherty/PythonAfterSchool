# import statements allow us to import code created by someone else
# the random package allows us to generate ranomness in our program
import random

# this line generates a random number between 0-200 and assigns it to the variable target_number
# Question: can the two edge numbers (0 & 200) be generated? Or is it just the numbers between 0 and 200 like (1, 2, 3, ..., 199)?
target_number = random.randrange(0, 200)

# This is a testing line, you can use it to see what the generated number is
print(target_number)

# a variable that represents the number of tries left 
number_of_tries_left = 10
# Create a while loop condition
while : #hint we need to check that the number of tries left is greater than 10

# This line will print out the number of tries left
    print("You have {} guesses left".format(number_of_tries_left) )

# This line will prompt the user to enter a guess
    guess = int(input("Please enter your guess: "))

# write code that fills in the rest

    # check if the guess is correct
    #if guess was correct, congragulate them and exit
    #if guess was not correct tell them to try again
    # decrease number of tries left by 1

    # what if the problem is too hard and we need to give them a hint?
    # usr_input = input("Would you like a hint? (y/n): ")
   
# Is this correct?
print("Sorry you ran out of tries, you lose the game")