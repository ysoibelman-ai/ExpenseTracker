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

class Outprints():
    @staticmethod
    def show_expenses (table):
        console = Console()
        console.print(table)

    @staticmethod
    def generate(total_category_dict):
        print (total_category_dict)