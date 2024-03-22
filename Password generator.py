#Passowrd Generator 

import random
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','#','$','%','&','*','^',')']

print("Welcome to the pyPassword Generator!")
n_letters = int(input("How many letters would you like in your password?\n "))
n_symbols = int(input("How many symbols would you like in your password?\n"))
n_numbers = int(input("How many numbers would you like?\n"))

#easy level 
password = ""
#n_letters = 4 as in the user chose 4 

for char in range(1, n_letters + 1):
    random_char = random.choice(letters)#we want to pick randomly from the leteers list using the .choice function
    # print(random_char)
    password += random_char

for char in range(1, n_symbols + 1):
    random_sym=random.choice(symbols)
    password+= random_sym


for char in range(1, n_numbers + 1):
    random_num=random.choice(numbers)
    password += random_num


# we add the password to what we generated. password is an empty string so just concatenate 
    

print(password)

#.shuffle()can be used to shuffle stuff
#random.shuffle




