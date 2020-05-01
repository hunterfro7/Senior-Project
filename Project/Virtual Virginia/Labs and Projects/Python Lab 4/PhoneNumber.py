###########################################################################################################
# Sara Student
# Project 4 - PhoneNumber.py
# This project creates a phone number based off of user input.
# Month Day, 20XX
###########################################################################################################


# This is where the core logic of code should go.
def main():
    # Use count and str_build variables to keep track of how many numbers have been input and building the phone number
    # respectively.
    count = 0
    str_build = "("
    # Collect the first three digits of the phone number.
    while count < 3:
        digit = int(input("Input a number 0-9: "))
        if digit >= 0 and digit <= 9:
            str_build += str(digit)
            count += 1
        # Handle a number being larger than 9 or less than 0.
        else:
            print("The number must be between 0-9.")
    # print("add ')' to the phone number
    str_build += ") "
    # get the next three digits of the phone number
    while count < 6:
        digit = int(input("Input a number 0-9: "))
        if digit >= 0 and digit <= 9:
            str_build += str(digit)
            count += 1
        else:
            print("The number must be between 0-9.")
    # Add ' - ' to the phone number
    str_build += " - "
    # add the last four digits of the phone number
    while count < 10:
        digit = int(input("Input a number 0-9: "))
        if digit >= 0 and digit <= 9:
            str_build += str(digit)
            count += 1
        else:
            print("The number must be between 0-9.")
    # output the phone number
    print(str_build)
    # Exit this function
    exit()


# This script looks for a function named "main" and runs the function.
if __name__ == "__main__":
    main()
