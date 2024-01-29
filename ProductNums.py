"""
File: ProductNums.py

Author: Brent Rushton

Version: 1.0

Description: 
Asks the user for two integers, multiplies them,
and returns the product.
"""

# Calculates the product
def CalculateProduct(num1, num2):
    return num1 * num2

def ProductNums():
    try:
        # Ask for input 
        num1 = int(input("Enter the first integer: "))
        num2 = int(input("Enter the second integer: "))
        
        # Call product function
        product = CalculateProduct(num1, num2)

        # Return Value
        print(f"The Product fo {num1} and {num2} is: {product}.")

    # Error Handling
    except ValueError:
        print("Invalid input! Please enter valid integers.")

# Call ProductNums
ProductNums()