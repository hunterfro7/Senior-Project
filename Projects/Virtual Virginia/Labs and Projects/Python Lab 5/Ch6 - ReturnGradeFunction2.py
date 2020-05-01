# Return the grade for the score 
def getGrade(score):
    if score >= 90.0:
        return 'A'
    elif score >= 80.0:
        return 'B'
    elif score >= 70.0:
        return 'C'
    elif score >= 60.0:
        return 'D'
    else:
        return 'F'

# Main method - asks for a numeric score to find a letter grade for
def main():
    score = eval(input("Enter a score: "))
    
    # Prints the letter grade passed back from the function call getGrade,
    # passing in the score
    letterGrade = getGrade(score)
    print("The grade is", letterGrade)

main() # Call the main function
