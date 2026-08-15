def total (expenses:list) -> float:
    total_amount = 0
    for expense in expenses:
        total_amount += int(expense.amount)
    return total_amount

def total_category(expenses:list, category:str):
    total_cost = 0
    for i in range (len(expenses)):
        if expenses[i].category == category:
            total_cost += int(expenses[i].amount)
    return total_cost

def total_by_category(expenses: list) -> dict:
    expense_dict = {}
    for expense in expenses:
        if expense.category in expense_dict:
            expense_dict[expense.category] += int(expense.amount)
        else:
            expense_dict[expense.category] = int(expense.amount)
    return expense_dict