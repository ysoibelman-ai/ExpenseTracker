from datetime import *
from rich.console import Console
from rich.table import Table
import questionary
from expenses import *
from expense import *
from expenses import *
from expense import *
from display import *
import typer

class Main:
    myexpenses = Expenses()
    app = typer.Typer()
    console = Console()

    @staticmethod
    @app.callback(invoke_without_command=True)
    def main(ctx: typer.Context):
        if ctx.invoked_subcommand is None:
            Main.not_cli()

    @staticmethod
    @app.command()
    def add(title,amount,category):
        expenses= Main.myexpenses
        expenses.add_expense_typer(title,amount,category)

    @staticmethod
    @app.command()
    def list(category = None):
        expenses= Main.myexpenses
        if not category:
            Outprints.show_expenses(expenses.create_table())
        else:
            Outprints.show_expenses(expenses.create_table(category))

    @staticmethod
    @app.command()
    def report():
       expenses= Main.myexpenses
       report = Outprints.generate(expenses.total_per_category())
       if type(report) == int and report > config.monthly_budget:
           Main.console.print("[bold red] WARNING: Your expenses are more than your monthly budget!!![/bold red]")

           pass
       
    def not_cli():
        expenses = Main.myexpenses
        add_expense = questionary.select("do you want to add an expense?",choices= [ "Yes","No"]).ask()
        while add_expense == "Yes":
            expenses.ask_for_expense()
            Outprints.show_expenses(expenses.create_table())
            add_expense = questionary.select("do you want to add another expense?",choices= [ "Yes","No"]).ask()

if __name__ == "__main__":
    Main.app()