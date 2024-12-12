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

# List of expenses
expenses = [
    {'amount':50, 'category':'food'},
    {'amount':20, 'category':'transfort'},
    {'amount':10, 'category':'entertainment'}
]

total, categories = calculate_expenses(expenses)
print(f"Total Expenses: ${total}")
print(f"Category Breakdow: {categories}")