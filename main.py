import random
# The computer randomly chooses between 1 (rock), 2 (paper), or 3 (scissors)
computer= random.choice([1,2,3])  

# Dictionary to map user's input to corresponding numeric value
dictionary={       
    "rock":1, 
    "paper":2, 
    "scissor":3 
}

# Dictionary to map numeric values back to the corresponding choice
reverse={          
    1:"rock",
    2:"paper",
    3:"scissor"
}
def game():
# Prompt the user to input their choice of rock, paper, or scissors
   user_choice=input("\n1.Rock 2.Paper 3.Scissor\nEnter your choice: ")  

# Convert user's choice (string) to its numeric equivalent
   user=dictionary[user_choice.lower()]

# Display the computer's choice using the reverse dictionary
   print(f"computer chose {reverse[computer]}")

# Determine the outcome of the game
   if(computer == user):
    print("It's a Draw!")  

   elif(computer == 1 and user == 2):
    print("You Win!")               # Paper covers Rock

   elif(computer == 1 and user == 3):
    print("You lose! Try again")    # Rock crushes Scissors

   elif(computer == 2 and user == 1):
    print("You lose! Try again")    # Paper covers Rock

   elif(computer == 2 and user == 3):
    print("You Win!")               # Scissors cuts Paper

   elif(computer == 3 and user == 1):
    print("You Win!")               # Rock crushes Scissors

   elif(computer == 3 and user == 2):
    print("You lose! Try again")    # Scissors cuts Paper

   again=input("Do you want to play again?\n(Yes/NO)?").lower()
   if(again=="yes"):
     game()
   else:
     print("Thank You! For playing")

game()