#calculator
def add(n1,n2):
    return n1 + n2
def subtraction(n1,n2):
    return n1 - n2

def multipication(n1,n2):
    return n1 *n2

def divide(n1,n2):
    return n1/n2

operations={
  "+":add,
  "-": subtraction,  #dictionary of operations 
  "*": multipication,
  "/": divide 

}

# function = operations["*"] #tapping into the dictionary and selecting the first key
# function(2,3)

num1 = int(input("What is the first number?: "))

#now we loop through the dictionary to find the keys for what the user wants to do
for symbol in operations:
   
    print(symbol) #we have saved all keys into a variable to be printed
should_continue = True
while should_continue:


 operation_symbol = input("Pick an operation from the line above: ")

 num2 = int(input("What is the second number?: "))

#we need to now pickout from the dictionary what sign the user chooses nb it is saved in a variable
 calculation_function= operations[operation_symbol]
 answer=calculation_function(num1,num2)

 print(f"{num1} {operation_symbol} {num2} = {answer}")

# operation_symbol = input("pick another operation: ")
# num3 = int(input("What is the next number?: "))
# calculation_function = operations[operation_symbol]

# second_answer = calculation_function(calculation_function(num1,num2), num3)
# print(f"{num1} {operation_symbol} {num3} = {second_answer}")

 if input(f"type 'y' to continue with {answer}, or type 'n' to exit: ") == 'y':
    num1 = answer
 else:
    should_continue = False    