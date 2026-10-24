# Breanna Murray
# October 23, 2026
# P4LAB2
# Use while loop and for loop together 

# Psuedocode
# Get Integer from User
# Determine if the interger is positive or negative
# If the integer is positive, display multiplication table
# If the integer is negative, tell user program cannot accept it
# Ask user if they want to run again?
# If yes, run the program again
# If no, end/exit the program

run_again = "Yes"

while run_again != "No":
    user_num = int(input("Please enter an integer: "))

    if user_num >= 0:
        #display multiuplication table for that value and range (1-12) 
        for item in range (1 , 13):
            print(f"{user_num} * {item} = {user_num * item}")
    else:
        print("This program does not handle negative numbers.")
    run_again = input("Would you like to run the program again?")


#Loop has broken. User entered 'no'
print("Program is ending....Goodbye!")