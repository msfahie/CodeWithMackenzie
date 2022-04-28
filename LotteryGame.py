'''
Title: Lottery Game
    Go to the following link to try out this code:
    programiz.com/python-programming/online-compiler/

In this Python script, we will be practicing making Python wait for a period of time just like how Scratch waits for a certain number of seconds.
We will also be practicing creating variables and picking random numbers like Scratch can do.
We will also be using an if-then-else statement to check if our numbers match the lottery winning numbers.
'''
# To use the time and random modules, we need the following import statements:
import time
import random

print("The lottery numbers you have are: ")

# Creating the variables for your numbers and giving the player a chance to enter the numbers they want:
myBall1 = input("What number would you like for your first ball? ")
myBall2 = input("What number would you like for your second ball? ")
myRedBall = input("What number would you like for your third ball? ")
# Making your numbers show in the output:
print("Great! Your numbers are: ", myBall1, myBall2, myRedBall)

# The game for selecting winning Lottery numbers:
print("Welcome to the lottery, the jackpot is $10,000.")

ball1 = random.randint(1,70)
time.sleep(1)
print("The first number is: ", ball1)

ball2 = random.randint(1,70)
time.sleep(1)
print("The second number is: ", ball2)

redBall = random.randint(1,26)
time.sleep(1)
print("The third number is: ", redBall)

time.sleep(3)

# Now for checking if the numbers match or not:
if myBall1 == ball1 and myBall2 == ball2 and myRedBall == redBall:
    print("You win!")
else:
    print("You did not win.")
