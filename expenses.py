from datetime import *
from rich.console import Console
from rich.table import Table
import questionary
from expenses import *
from expense import *
from expenses import *
from expense import *
from display import *

class Expenses:
    def __init__(self):
        self.expense_list = []

    def add_expense(self,expense:dict):
        today = str(date.today())
        self.expense_list.append(Expense(today,expense["title"],expense["category"],expense["amount"]))

    def add_expense_typer(self,title,amount,category):
        today = str(date.today())
        self.expense_list.append(Expense(today,title,category,amount))

    def ask_for_expense(self):
        expense = {}
        expense["title"] = questionary.text("enter title").ask()
        expense["amount"] = questionary.text("enter amount").ask()
        expense["category"] = questionary.select("what category is the expense",choices =["Food","Travel","School","Entertainment","other"]).ask()
        self.add_expense(expense)

    def calc_total (self, category= None):
        total_cost = 0
        expenses = self.expense_list
        if len(expenses) == 0:
            return 0
        if not category:
            for i in range (len(expenses)):
                total_cost += int(expenses[i].amount)
        else:
            for i in range (len(expenses)):
                if expenses[i].category == category:
                    total_cost += int(expenses[i].amount)
        return total_cost

    def total_per_category(self):
        total = {}
        expenses = self.expense_list
        if len(expenses) > 0:
            for expense in expenses:
                if expense.category not in total:
                    total [expense.category] = expense.amount
                else:
                    total[expense.category] += expense.amount
            return total
        else:
            return "No items in list" 

    def create_table(self,category = None):
            expenses = self.expense_list
            today = str(date.today())
            table = Table(title = "Expenses")
            table.add_column("Date",no_wrap=True)
            table.add_column("Title",no_wrap=True)
            table.add_column("Category",no_wrap=True)
            table.add_column("Amount",no_wrap=True)
            if not category:
                for expense in expenses:
                    table.add_row(today,expense.title,expense.category,expense.amount)
                table.caption = f"Toal Amount: {self.calc_total()}$"
                return table
            else:
                for expense in expenses:
                    if expense.category == category:
                        table.add_row(today,expense.title,expense.category,expense.amount)
                table.caption = f"Toal Amount: {self.calc_total()}$"
                return table