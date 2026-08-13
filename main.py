from datetime import *

class Expenses:
    def __init__(self):
        self.expense_list = []

    def add_expense(self,expense:dict):
        today = date.today()
        self.expense_list.append(Expense(today,expense["title"],expense["category"],expense["amount"]))

    def ask_for_expense(self):
        expense = {}
        expense["title"] = input("enter title: ")
        expense["category"] = input("enter category: ")
        expense["amount"] = int(input("enter amount: "))
        self.add_expense(expense)

    def show_expenses (self):
        expenses = self.expense_list
        print ("Your Expenses:")
        if len(expenses) >= 1:
            for i in range (len(expenses)):
                print  (f"Date: {expenses[i].date}\nTitle: {expenses[i].title}\nCategory: {expenses[i].category}\nAmount: {expenses[i].amount}\n")
            print(f"Total Amount: {self.calc_total()}$")
        else:
            print ("You have no expenses")

    def calc_total (self):
        total_cost = 0
        expenses = self.expense_list
        if len(expenses) == 0:
            return 0
        for i in range (len(expenses)):
            total_cost += expenses[i].amount
        return total_cost

class Expense:
    def __init__(self,date,title,category,amount):
        self.date = date
        self.title = title
        self.category = category
        self.amount = amount

class Main:
    myexpenses = Expenses()
    myexpenses.show_expenses()
    add_expense = input("eneter 1 to add express, to exit enter anything else: ")
    while add_expense == "1":
        myexpenses.ask_for_expense()
        myexpenses.show_expenses()
        add_expense = input("enter 1 to add another expense, to exit enter anything else: ")


Main()
