from datetime import *
from rich.console import Console
from rich.table import Table
import questionary
from expenses import *
from expense import *
from expenses import *
from expense import *
from display import *



class Main:
    myexpenses = Expenses()
    add_expense = questionary.select("do you want to add an expense?",choices= [ "Yes","No"]).ask()
    while add_expense == "Yes":

        myexpenses.ask_for_expense()
        Outprints.show_expenses(myexpenses.create_table())
        add_expense = questionary.select("do you want to add another expense?",choices= [ "Yes","No"]).ask()

Main()
