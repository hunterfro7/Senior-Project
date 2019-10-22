import random

#Step One
x = 0
count = 0
num = 0
for x in range(7):
    print("Input a number : ")
    num = num + int(input())
    count = count + 1
average = num/count
print(average)
#Step Two
print("Input a number : ")
numOne = int(input())
print("Input a number : ")
numTwo = int(input())
print(round(numOne/numTwo))
print(numOne%numTwo)
#Step Three
nOne = int(random.randint(1,13))
nTwo = int(random.randint(1,13))
print(nOne)
print(nTwo)
nProduct = nOne * nTwo
uProduct = int(input("Enter the product of these numbers : "))
if nProduct == uProduct:
    print("Correct!")
else:
    print("Wrong!")