# Function of Options     
def option():
    print()
    print("Welcome To My Calculator Project")
    options = ["----------------------","Select Operation.", "----------------------", "1. Addition", "2. Subtraction",
           "3. Multiplication", "4. Division"]
    for i in options:
        print(i)
option() 

# Define a Operations
def add(x, y):print("Addition is :", x+y)
def sub(x, y):print("Subtraction is :", x-y)
def mul(x, y):print("Multiplication is :", x*y)
def div(x, y):print("Division is :","{:.2f}".format(x/y))

while True:
    #input for choice from the user 
    choice = input("Enter Choice [1/2/3/4]: ")
    print()
    if choice>"0" and '4'>=choice:
        #take input from the user
        x,y = float(input("Enter first number: ")), float(input("Enter second number: "))
        #calculation part
        calculations = add(x, y) if (choice == "1") or (choice == "add") else sub(x, y) if (choice == "2") or (choice == "sub") else mul(x, y) if (choice == "3") or (choice == "mul") else div(x, y) if (choice == "4") or (choice == "div") else "Sorry, Invalid input please try again"
    
    else:
        print("range is over")

    # break the while loop if answer is no
    print()
    next_cal = input("Let's do next calculation? (yes/no): ")
    if (next_cal == "Yes") or (next_cal == "yes") or (next_cal == "YES") or (next_cal == "Y") or (next_cal == "y"):
        continue
    elif (next_cal == "No") or (next_cal == "no") or (next_cal == "NO") or (next_cal == "N") or (next_cal == "n"):
        break
    else:
        print("Invalid command")
        break
     
         
    