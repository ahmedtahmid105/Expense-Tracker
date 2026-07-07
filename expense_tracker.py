print("Welcome to the Daily Expense Tracker!")

print("\nMenu:")
print("1. Add a new expense")
print("2. View all expenses")
print("3. Calculate total and average expense")
print("4. Clear all expenses")
print("5. Exit")

expense_list = None
while True:
    choice = int(input())

    if choice == 5:
        print("Exiting the Daily Expense Tracker. Goodbye!")
        break
    elif choice == 1 :
        expense_list = float(input())
        print ("Expense added successfully!")