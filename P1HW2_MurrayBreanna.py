# Breanna Murray
# September 26, 2026
# P1HW2 - Travel Expense Calculator 
# Calculating the remaining budget after travel expenses.
# Displays travel destination, total expenses, and remaining budget using a formatted output.

# Pseudocode:
# Enter their budget.
# Ask travel destination.
# Ask gas expense.
# Ask accommodation expense.
# Ask about their food expense.
# Add the gas, accommodation, and food expenses.
# Subtract the total expenses from the budget.
# Display the formatted travel destination, total expenses, and remaining budget

budget = float(input("Enter your budget: "))
destination = input("Enter your travel destination: ")
gas = float(input("Enter amount you will spend on gas: "))
accommodation = float(input("Enter amount you will spend on accommodation: "))
food = float(input("Enter amount you will spend on food: "))

# Calculate the total expenses.
total_expenses: float = gas + accommodation + food
# Calculate the remaining budget.
remaining_budget: float = budget - total_expenses

# Results
print()
print("Travel Expenses")
print(f"Travel Destination", destination)
print(f"Initial Budget", budget)
print(f"Gas", gas)
print(f"Accommodation", accommodation)
print(f"Food", food)
print(f"Total Expenses", total_expenses)
print(f"Remaining Budget", remaining_budget)