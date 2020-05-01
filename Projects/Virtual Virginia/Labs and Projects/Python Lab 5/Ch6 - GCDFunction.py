# Return the gcd of two integers 
def gcd(n1, n2):
    gcd = 1 # Initial gcd is 1
    k = 2   # Possible gcd

    while k <= n1 and k <= n2:
        if n1 % k == 0 and n2 % k == 0:
            gcd = k # Update gcd
        k += 1

    return gcd # Return gcd

# Main method - asks for two numbers to find the gcd of
def main():
    num1 = eval(input("Enter the first number: "))
    num2 = eval(input("Enter the second number: "))
    # Prints the GCD passed back from the function call gcd,
    # passing in num1 and num2
    print("The gcd is", gcd(num1, num2))

main() # Call the main function
