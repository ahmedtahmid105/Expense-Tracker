print ("Welcome to the Daily Expense Tracker!")
print("\nMenu:")
print("1. Add a new expense")
print("2. View all expenses")
print("3. Calculate total and average expense")
print("4. Clear all expenses")
print("5. Exit")
expense_list = []
while True :
    choose_option = input()
    if choose_option == "5" :
        print ("Exiting the Daily Expense Tracker. Goodbye!")
        break
    elif choose_option == "1" :
        x = float(input())
        expense_list.append(x)
        print("Expense added successfully!")
    elif choose_option == "2" :
        if expense_list == [] :
            print ("No expenses recorded yet.")
        else :
            print ("Your expenses:")
            for index, value in enumerate (expense_list,1) :
                print (f'{index}. {value}')
    elif choose_option ==  "3" :
        if expense_list == [] :
            print ("No expenses recorded yet.")
        else :
            total = sum(expense_list)
            average = total / len(expense_list)
            print(f"Total expense: {total}")
            print(f'Average expense: {average}')
    elif choose_option == "4" :
        expense_list.clear()
        print("All expenses cleared.")