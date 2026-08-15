from datetime import *
from rich.console import Console
from rich.table import Table
import questionary
from expenses import *
from expense import *
from expenses import *
from expense import *
from display import *
from helpers import *
import config

class Expenses:
    console = Console()
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

    def calc_total (self):
        expenses = self.expense_list
        total_cost = total (expenses)
        return total_cost

    def total_of_category(self, category):
        expenses = self.expense_list
        total = total_category (expenses,category)
        return total

    def total_per_category(self):
        expenses = self.expense_list
        expense_list = total_by_category(expenses)
        if len (expense_list) > 0:
            return expense_list
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
                    table.add_row(today,expense.title,expense.category,expense.amount+config.currency)
                table.caption = f"[bold #CCFF00]Total Amount: {self.calc_total()}{config.currency}[/bold #CCFF00]"
                return table
            else:
                for expense in expenses:
                    if expense.category == category:
                        table.add_row(today,expense.title,expense.category,expense.amount+config.currency)
                table.caption = f"[bold #CCFF00]Total Amount: {self.calc_total()}{config.currency}[/bold #CCFF00]"
                return  table