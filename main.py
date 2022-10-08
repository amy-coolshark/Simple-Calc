# Simple-Calc
# Assignment 1 of CSU33012 - Group 50
# Collaborators: Abigail Amethyst, Liam Junkermann


# calc
# Calculates a passed String and returns the result in the form of an integer (FUNCTION ASSUMES VALID INPUT)
# This works by converting the infix expression into a postfix one, and then evaluating it
# Author: Abigail Amethyst
# s - User Input String
# returns the result of mathematical expression
def calc(s):
    precedence = {'+': 1, '-': 1, '*': 2}
    s = s.replace(" ", "")
    stack = []
    postfix = ""
    # converting infix expression to postfix
    for i in s:
        if i == "+" or i == "-" or i == "*":
            postfix += ","
            while stack and precedence[i] <= precedence[stack[-1]]:
                postfix += stack.pop()
            stack.append(i)
        else:
            postfix += i
    while stack:
        postfix += ","
        postfix += stack.pop()

    # calculating postfix expression
    operand = ""
    for i in postfix:
        if i == "+" or i == "-" or i == "*":
            int2 = stack.pop()
            int1 = stack.pop()
            if i == "+":
                result = int1 + int2
            elif i == "-":
                result = int1 - int2
            else:
                result = int1 * int2
            stack.append(result)
        elif i == ",":
            try:
                stack.append(int(operand))
                operand = ""
            except ValueError:
                continue
        else:
            operand += i

    result = stack.pop()
    return result


# userInput
# Prompts the user to input an equation to be calculated and returns the string of the user input
# Author: Abigail Amethyst
def userInput():
    return input("Please enter a mathematical expression you would like the program to perform or type exit: ")


# checkInput
# Checks that user input is valid
# Author: Liam Junkermann
# s - input string collected from userInput()
# returns the string, or throws an error
def checkInput(s):
    allowedChars = ['0', '1', '2', '3', '4',
                    '5', '6', '7', '8', '9', '+', '-', '*', ' ']
    operators = ['+', '-', '*']
    if len(s) > 0:
        for idx in range(0, len(s)):
            try:
                # Checking if current char is allowed char
                allowedChars.index(s[idx])
                if idx > 0:
                    if s[idx] in operators and s[idx] == s[idx-1]:
                        raise Exception("Double Operator Found")
            except ValueError:
                raise Exception("Unexpected character passed")
        # print('valid string, returning')
        return s
    else:
        raise Exception("No input entered")


# Main
if __name__ == "__main__":
    print("Welcome to the Simple-Calc program written for CSU33012 Software Engineering.")
    print("This program only does calculation, subtraction and multiplication. Please do not enter any operands other "
          "than that, otherwise the program will throw an error.")
    while True:
        try:
            inp = userInput()
            if inp == "exit":
                break
            print(calc(checkInput(inp)))
        except Exception as e:
            print(e)
