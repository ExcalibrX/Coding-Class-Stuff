print("Welcome to the Expense Tracker!\n")

expenses = [] # list to store expenses

def add(): 
    # function to add an expense
    item = input("Enter Expense: ")
    amount = float(input("Enter the amount: "))
    
    # saving expense as a dictionary (item and amount)
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
            print(f"Item: {expense['item']}, Amount: ${expense['amount']}") # display all expense
        print(f"Total Expenses: ${sum(expense['amount'] for expense in expenses)}")

def edit():
    # function to edit an expense
    item = input("Enter the expense you would like to edit: ")
    for expense in expenses:
        if expense['item'] == item: # find the expense to edit
            new_item = input("Enter new expense name: ")
            new_amount = float(input("Enter new amount: "))
            expense['item'] = new_item
            expense['amount'] = new_amount
            print("Expense updated successfully!")
            return
    print("Expense not found. Enter another expense.\n") # handling case where expense is not found


def delete(): 
    # function to delete an expense
    item = input("Enter the expense you would like to delete: ")
    for expense in expenses:
        if expense['item'] == item: # find the expense to delete
            expenses.remove(expense)
            print("Expense deleted successfully!")
            return
    print("Expense not found. Enter another expense.\n") # handling case where expense is not found


def summary():
    # function to show summary of expenses
    for expense in expenses:
        total = sum(expense['amount'] for expense in expenses)
        print(f"Your total expenses are: ${total}")
        return
    print("No expenses to summarize.\n") # handling case where there are no expenses

while True: 
    # main loop
    print("Options:")   # display menu options
    print("1. Add Expense") # enter into add expense
    print("2. View Expenses") # enter into view expenses
    print("3. Edit Expense") # enter into edit expense
    print("4. Delete Expense") # enter into delete expense
    print("5. Summary") # enter into summary
    print("6. Exit") # exit the program
    
    choice = input("Choose an option (1-5): ") # get user choice
    
    if choice == '1':
        add()
    elif choice == '2':
        view()
    elif choice == '3':
        edit()
    elif choice == '4':
        delete()
    elif choice == '5':
        summary()
    elif choice == '6':
        print("Thank you for using my expense tracker, Goodbye!") 
        break # exit the loop
    else:
        print("Invalid choice. Please select a valid option (1-6).")  # handling invalid input
