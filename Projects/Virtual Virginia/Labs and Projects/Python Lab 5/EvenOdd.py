###########################################################################################################
# Sara Student
# Project 5 - EvenOdd.py
# This project creates a phone number based off of user input.
# Month Day, 20XX
###########################################################################################################


# if number mod 2 equals zero then the number is even so return true else return false because the number is odd.
def even(num):
    if (num % 2) == 0:
        return True
    else:
        return False


# This is where the core logic of code should go.
def main():
    # Get user input
    num = int(input("Input a number: "))
    # If the number is even output that it is even else output that the number is odd
    if even(num):
        print("The number is even")
    else:
        print("The number is odd")
    # Exit this function
    exit()


# This script looks for a function named "main" and runs the function.
if __name__ == "__main__":
    main()
