"""
File: SquareNum.py

Author: Brent Rushton

Version: 1.0

Description: 
Asks the user for an integer, squares it, returns to user.
"""

# Calculates the product
def CalculateSquare(num):
    return num * num

def SquareNum():
    try:
        # Ask for input 
        num = int(input("Enter an integer: "))
        
        # Call product function
        square = CalculateSquare(num)

        # Return Value
        print(f"The square of {num} is {square}")

    # Error Handling
    except ValueError:
        print("Invalid input! Please enter a valid integer.")
        SquareNum()

# Call ProductNums
SquareNum()