import random

#Generate two random integers
number1 = random.randint(0, 9)
number2 = random.randint(0, 9)

#If number1 < number2, swap number1 and number2
if number1 < number2:
    number1, number2 = number2, number1

#Prompt the student to answer "What is number1 - number2
answer = eval(input("What is " + str(number1) + " - " + str(number2) + "? "))

#Repeatedly ask the student the question until the answer is correct
while number1 - number2 != answer:
    answer = eval(input("Wrong answer.  Try again. What is "
                        + str(number1) + " - " + str(number2) + "? "))

#Display message that you succeeded
print("You got it!")
