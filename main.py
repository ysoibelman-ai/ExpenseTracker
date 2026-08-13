from datetime import *
from rich.console import Console
from rich.table import Table
import time

class Expenses:
    def __init__(self):
        self.expense_list = []

    def add_expense(self,expense:dict):
        today = str(date.today())
        self.expense_list.append(Expense(today,expense["title"],expense["category"],expense["amount"]))

    def ask_for_expense(self):
        expense = {}
        expense["title"] = input("enter title: ")
        expense["category"] = input("enter category: ")
        expense["amount"] = input("enter amount: ")
        self.add_expense(expense)

    def show_expenses (self):
        today = str(date.today())
        expenses = self.expense_list
        console = Console()
        table = Table(title = "Expenses")

        table.add_column("Date",no_wrap=True)
        table.add_column("Title",no_wrap=True)
        table.add_column("Category",no_wrap=True)
        table.add_column("Amount",no_wrap=True)
        for expense in expenses:
            table.add_row(today,expense.title,expense.category,expense.amount)
        table.caption = f"Toal Amount: {self.calc_total()}"
        console.print(table)

    def calc_total (self):
        total_cost = 0
        expenses = self.expense_list
        if len(expenses) == 0:
            return 0
        for i in range (len(expenses)):
            total_cost += int(expenses[i].amount)
        return total_cost
        
class Expense:
    def __init__(self,date,title,category,amount):
        self.date = date
        self.title = title
        self.category = category
        self.amount = amount

class Main:
    myexpenses = Expenses()
    add_expense = input("eneter 1 to add express, to exit enter anything else: ")
    while add_expense == "1":
        myexpenses.ask_for_expense()
        myexpenses.show_expenses()
        add_expense = input("enter 1 to add another expense, to exit enter anything else: ")


Main()
