# Incorporate the random library
import random

# Print Title
print("Let's Play Rock Paper Scissors!")

# Specify the three options
options = ["r", "p", "s"]

# Computer Selection
computer_choice = random.choice(options)

# User Selection
user_choice = input("Make your Choice: (r)ock, (p)aper, (s)cissors? ")

# Run Conditionals

If (user_choice == "p" and computer_choice == "p"):
    print("you entered p and the computer chose p")
    print("it is a tie")

elif (user_choice == "p" and computer_choice == "r"):
    print("you entered p and the computer chose r")
    print("you win")

elif (user_choice == "p" and computer_choice == "s"):
    print("you entered p and the computer chose s")
    print("The computer wins")

elif (user_choice == "r" and computer_choice == "s"):
    print("you entered r and the computer chose s")
    print("you win")

elif (user_choice == "r" and computer_choice == "r"):
    print("you entered r and the computer chose r")
    print("it is a tie")

elif (user_choice == "r" and computer_choice == "p"):
    print("you entered r and the computer chose p")
    print("The computer wins")

elif (user_choice == "s" and computer_choice == "s"):
    print("you entered s and the computer chose s")
    print("it is a tie")

elif (user_choice == "s" and computer_choice == "r"):
    print("you entered s and the computer chose r")
    print("The computer wins")
    
elif (user_choice == "s" and computer_choice == "p"):
    print("you entered s and the computer chose p")
    print("you win")