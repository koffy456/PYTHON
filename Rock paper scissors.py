#rock paper scissors using randomization
import random
user_choice = int(input("What do you choose. 0 for rock, 1 for paper or 2 for scissors\n"))

#the computer choice is next which is a random number
computer_choice = random.randint(0,2)
print(f"Computer chose {computer_choice}")



if user_choice >= 3 or user_choice<0:
    print("You typed a wrong number..you lose!")
elif user_choice == 0 and computer_choice == 2:
    print("You win!!")
elif computer_choice== 0 and user_choice==2:
    print("You lose")
elif computer_choice > user_choice:
    print("You lose!!")
elif user_choice > computer_choice:
    print("You win")
elif computer_choice == user_choice:
    print("It's a draw")
