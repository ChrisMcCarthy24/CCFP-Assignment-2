"""
File: SumNums.py

Author: Chris McCarthy

Version: 1.0

Description: 
Asks the user for two integers adds them
and returns the result.
"""

# Calculates the sum
def CalculateSum(vNum1, vNum2):
    return vNum1 + vNum2

def sumNums():
    try:
        # Ask for input 
        vNum1 = int(input("Enter the first integer: "))
        vNum2 = int(input("Enter the second integer: "))
        
        # Call sum function
        vSum = CalculateSum(vNum1, vNum2)

        # Return sum
        print(f"The Product of {vNum1} and {vNum2} is: {vSum}")

    # Error Handling
    except ValueError:
        print("Invalid input! Please enter valid integers.")

# Call sumNums
sumNums()