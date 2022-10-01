# TODO: implement printing input prompts and outputs
# TODO: error checking for invalid inputs
# TODO: unit testing


# Calc
# Calculates a passed String and returns the result in the form of an integer
# Author: Abigail Amethyst
# s - User Input String
def calc(s):
    s.replace(" ", "")
    return eval(s)


# Main
if __name__ == "__main__":
    print("Welcome to the Simple-Calc program written for CSU33012 Software Engineering.")
    print("This program only does calculation, subtraction and multiplication. Please do not enter any operands other "
          "than that, otherwise the program will throw an error.")
    inp = input("Please enter a calculation you would like the program to perform:\n")
    print(calc(inp))
