'''
At his project we will an expense tracker app where users can input their monthly expenses. 
You need to calculate the total expense and categorize them(e.g. food, transpoert, entertainment).
'''

def calculate_expenses(expenses):
    total = sum(expense['amount'] for expense in expenses) # Run loop and take the value of amount from the expense list and make the sum
    categories = {} # Declear a Dictionary to keep all the expense history
    
    # Here we run a loop that check the category is already in categories dictionary? if it is we just increase the amount, other wise add a new one
    for expense in expenses:
        if expense['category'] in categories:
            categories[expense['category']] +=expense['amount']
        else:
            categories[expense['category']] = expense['amount']
    
    return total, categories

# Function to take the input from user
def get_user_input():
    expenses = []
    while True:
        try:
            # Take user input for amount and category
            category = input("Enter the expense category (e.g., food, transport): ").strip().lower()
            amount = float(input("Enter the expense amount (or type 'done' to finish): "))

            # Validate the category and amount
            if category == "":
                print("Category cannot be empty. Please try again.")
                continue
            
            # Add expense to the list
            expenses.append({'amount': amount, 'category': category})

        except ValueError:
            # Check if the user typed 'done' to exit or an invalid input was entered
            user_input = input("Enter the expense amount (or type 'done' to finish): ").strip().lower()
            if user_input == "done":
                break
            else:
                print("Invalid input. Please enter a valid number for the expense amount.")
                continue

    return expenses

# Main execution
expenses = get_user_input()
total, categories = calculate_expenses(expenses)

# Output the results
print(f"\nTotal Expenses: ${total}")
print("Category Breakdown:")
for category, amount in categories.items():
    print(f"- {category.capitalize()}: ${amount}")