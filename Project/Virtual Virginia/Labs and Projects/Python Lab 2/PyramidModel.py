# imports
import math


# This is where the core logic of code should go.
def main():
    print("Sara Student\nProject 2 - PyramidModel.py\nThis project displays the area and costs of building a model of a"
          "rectangular pyramid.\nMonth Day, 20XX")
    base_length = float(input("Enter the length of the base_length of the pyramid (inches): "))
    height = float(input("Enter the height of the pyramid (inches): "))
    print("The Sara's Metal Art surface area calculations are: ")
    slant_length = math.sqrt((0.5 * base_length) * (0.5 * base_length) + (height * height))
    surface_area = (base_length * base_length) + (0.5 * 4 * base_length * slant_length)
    price = surface_area * 1.32
    print("  Surface area of the pyramid: " + str(round(surface_area, 2)) + " square inches")
    print("  Total cost of the material is $" + str(round(price, 2)))
    exit()


# This script looks for a function named "main" and runs the function.
if __name__ == "__main__":
    main()