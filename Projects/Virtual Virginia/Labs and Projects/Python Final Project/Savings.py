###########################################################################################################
# Sara Student
# Final Project - Savings.py
# This project creates a phone number based off of user input.
# Month Day, 20XX
###########################################################################################################


# return true if the number is greater than or equal to 25 else return false
def discount(num):
    if num >= 25:
        return True
    else:
        return False


# This is where the core logic of code should go.
def main():
    while True:
        # Get user input
        num = int(input("Enter a number: "))
        # If the number is -1 then exit the loop and program
        if num == -1:
            print("Goodbye")
            # Exit this function
            exit()
        # If the discount is true the multiply num by 3.5 for the final cost
        if discount(num):
            total_cost = num * 3.50
            print("The total cost of the bulbs is $" + str(total_cost) + "0")
        # If discount is false multiply num by 5 then output final cost
        else:
            total_cost = num * 5.00
            print("The total cost of the bulbs is $" + str(total_cost) + "0")
    # Exit this function
    exit()


# This script looks for a function named "main" and runs the function.
if __name__ == "__main__":
    main()
