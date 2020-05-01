# Sara Student
# Project 3 - ClubDecisions.py
# This project displays the price for members and non-members to get into a club based off of age.
# Month Day, 20XX

# note - This program does not handle upper-case or strange inputs very well, it is not expected that new programmers
# handle errors like that this early in their programming experience.


# This is where the core logic of code should go.
def main():
    # Get user input for membership status then get user input for age -------------------------------------------------
    membership_status = input("Enter your membership status: ")
    age = int(input("Enter your age: "))
    # Get user input for membership status then get user input for age -------------------------------------------------
    # If user is a member and 21 or over return cost of $21.00 ---------------------------------------------------------
    if str(membership_status) == "member" and age >= 21:
        print("Club cost is $21.00")
    # If user is a member and 21 or over return cost of $21.00 ---------------------------------------------------------
    # Else if the user is a member and under 21 return cost of $12.00---------------------------------------------------
    elif str(membership_status) == "member" and age < 21:
        print("Club cost is $12.00")
    # Else if the user is a member and under 21 return cost of $12.00---------------------------------------------------
    # Else if the user is not a member and 21 or older return cost of $29.00--------------------------------------------
    elif str(membership_status) != "member" and age >= 21:
        print("Club cost is $29.00")
    # Else if the user is not a member and 21 or older return cost of $29.00--------------------------------------------
    # Else if the user is not a member and under 21 return cost of $16.00-----------------------------------------------
    elif str(membership_status) != "member" and age < 21:
        print("Club cost is $16.00")
    # Else if the user is not a member and under 21 return cost of $16.00-----------------------------------------------
    # Else there has been an issue in the logic that is unexpected------------------------------------------------------
    else:
        print("Invalid input, please try again.")
    # Else there has been an issue in the logic that is unexpected------------------------------------------------------
    # Exit this function
    exit()


# This script looks for a function named "main" and runs the function.
if __name__ == "__main__":
    main()
