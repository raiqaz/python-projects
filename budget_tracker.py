#set your monthly budget
STARTING_BUDGET=int(input("Enter your monthly budget: "))
#Ask for today's expenses
item=input("what did you buy today?")
cost=int(input(f"how much did the {item} cost?"))
#Save the new  expense to the file
with open("expenses.txt", "a") as file:
    file.write(f"{item}: {cost}\n")
# Now, let's calculate how much is used and how much is left in the budget
total_spent=0
#Open file in read mode("r")
with open("expenses.txt", "r") as file:
    for line in file:
        # If the line is empty, skip it
        if not line.strip():
            continue
        # Split the line into item and cost
        parts=line.strip().split(":")
        expense_cost=int(parts[1])
        #Add it to our cost
        total_spent+=expense_cost
#Calculate how much is left in the budget
remaining_budget=STARTING_BUDGET-total_spent
#Print the results
print(f"Total spent: ${total_spent}")
print(f"Remaining budget: ${remaining_budget}")
