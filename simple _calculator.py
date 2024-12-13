'''
Description: Create a simple calculator that can add, subtract, multiply, and divide two numbers based on user input.
'''

# Functions for calculate
def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): return x / y

def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    while True:
        # Give a option to user choosing either add or sub or multiply or divide. if user choose worng able to try once again unlit choose right one
        choice = input("Enter choice (1/2/3/4): ")
        if choice in ['1', '2', '3', '4']:
            break
        else:
            print("Invalid input! Please select 1, 2, 3, or 4.")     
    
    while True:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            if choice == '1':
                print(f"The result is: {add(num1, num2)}")
            elif choice == '2':
                print(f"The result is: {subtract(num1, num2)}")
            elif choice == '3':
                print(f"The result is: {multiply(num1, num2)}")
            elif choice == '4':
                if num2 != 0:
                    print(f"The result is: {divide(num1, num2)}")
                else:
                    print("Cannot divide by zero!")
            break
        except ValueError:
            print("Invalid input! Please enter numerical values.")

calculator()