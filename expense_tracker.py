expenses = [
    {"amount" : "50", "category" : "groceries"},
    {"amount" : "120", "category" : "Transport"}    
]

def add_expenses(amount, category):
    expenses.append({"amount" : amount, "category" : category})
    print(f"Added expense : {category} - {amount} ")

def show_expenses(expenses):
    if expenses:
        print("All expenses")
        for exp in expenses:
            print(f"{exp['category']} : {exp['amount']}")
    else:
        print("No expenses recorded")

def total_expenses(expenses):
    return sum(exp['amount'] for exp in expenses)

def average_expense(expenses):
    if expenses:
        return total_expenses(expenses) / len(expenses)
    return 0

def biggest_expenses(expenses):
    if expenses:
        return max(expenses, key = lambda x : x['amount'])
    return None

def remove_expense(amount, category):
    for exp in expenses:
        if exp['amount'] == amount and exp['category'] == category:
            expenses.remove(exp)
            print(f"Removed expense : {category} - {amount}")
            return
        print("Expense not found")
        

add_expenses( 50, "Food")
add_expenses( 120, "Transport")
add_expenses( 30, "Snacks")
remove_expense(120, 'Transport')

show_expenses(expenses)
print("Total:", total_expenses(expenses))
print("Average:", average_expense(expenses))
print("Biggest expense:", biggest_expenses(expenses))
