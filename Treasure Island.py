#ascii.co.uk/art

print("Welcome to treasure Island.")
print("Your mission is to find the treasure.")
choice1 = input('You\'re at a crossroad, where do you want to pass? "left" or "right". \n').lower()#\ is used to dodge code and remain text
#the.lower()function changes the user input into lowercase


if choice1 == "left":
    choice_2=input('You\'ve come to a lake. There is an island. Type "wait" or type "swim" to move\n').lower()

    if choice_2 == "wait":
       choice3 = input("You are at the island now and there are three doors choose between red yellow and blue\n").lower()
    
       if choice3 == "red":
         print("Room is full of fire. Game over!")
       elif choice3 == "yellow":
         print("You found the treasure. You win")
       elif choice3 == "blue" :
          print("You are dead ")
       else:
          print("You chose a non-existent door. Dead")
          
    else:
        print("You got attacked. Dead")
else:
    print("You fell, Game over!!")    
