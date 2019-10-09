import time
import sys
import lesson3_helpers as _l3

# Retrieves the current terminal window size in characters
#   i.e. 80 columns means the window is 80 characters wide
columns, rows = _l3.get_terminal_size()

# Initialize this variable before our loop
space = " "

# Step 1: change this variable assignment so that the arrow traverses
#   ALL the available columns
steps = int(columns / 4)

for i in range(steps):
    time.sleep(0.1)
    sys.stdout.write("\r")
    for j in range(i):
        sys.stdout.write(space)
    sys.stdout.write(">")
    sys.stdout.flush()

# Challenge: Uncomment the code below and complete the loop
#   logic to ensure the arrow reaches the beginning again

# Hint: If it takes three hops to get from point A to point B,
#   how many hops does it take to get from point B back to point A?
# while """insert variable to test here""" >= 0:
#     time.sleep(0.1)
#     sys.stdout.write("\r")
#     for j in range(steps):
#         sys.stdout.write(space)
#     """Subtract 1 from the variable used in the while conditional here"""
#     sys.stdout.write("<")
#     sys.stdout.flush()

print('\nEnd!\n')

# Step 2: make the below 'while' loop run forever

# Step 3: substitute the 'forever' condition for a decreasing counter.
#   Challenge: be creative with the condition, if you dare!

j = 0
# while """1 + 1 = 2""":
#     for j in range(6):
#         string = "[" + (j * " ") + "=" + (6 - j) * " " + "]"
#         sys.stdout.write("\r" + string)
#         sys.stdout.flush()
#         time.sleep(0.2)
#     for j in range(6):
#         string = "[" + (6 - j) * " " + "=" + (j * " ") + "]"
#         sys.stdout.write("\r" + string)
#         sys.stdout.flush()
#         time.sleep(0.2)
