print("Welcome to the Expense Tracker!\n")

expenses = [] # list to store expenses

def add(): 
    # function to add an expense
    item = input("Enter Expense: ")
    amount = float(input("Enter the amount: "))
    
    expense = {  
        "item": item,
        "amount": amount,
    }
    
    expenses.append(expense) # add expense to list
    print("Expense added successfully!") 

def view(): 
        # function to view all expenses
        if not expenses:
            print("No expenses in tracker, please enter an expense.")
            return
        for expense in expenses:
            print(f"Item: {expense['item']}, Amount: ${expense['amount']}")
        print(f"Total Expenses: ${sum(expense['amount'] for expense in expenses)}")

def delete(): 
    # function to delete an expense
    item = input("Enter the expense you would like to delete: ")
    for expense in expenses:
        if expense['item'] == item:
            expenses.remove(expense)
            print("Expense deleted successfully!")
            return
    print("Expense not found. Enter another expense.")

while True: 
    # main loop
    print("Options:")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Delete Expense")
    print("4. Exit")
    
    choice = input("Choose an option (1-4): ") # get user choice
    
    if choice == '1':
        add()
    elif choice == '2':
        view()
    elif choice == '3':
        delete()
    elif choice == '4':
        print("Thank you for using my expense tracker, Goodbye!") 
        break # exit the loop
    else:
        print("Invalid choice. Please select a valid option.")  # handle invalid input