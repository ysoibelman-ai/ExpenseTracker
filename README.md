Program name: Expense Tracker
Short Description:
This program is an expense tracker; it allows you to submit and calculate different expenses that you have from different categories. The program can also report back to you your total expense per category, in total or the total expense of a specific category. The expenses will be shown in a table which will include the date of each expense you submit with a total amount printed bellow the table. Note: there is an option to add expense and print out your report and total straight from the CLI.

Installation
1-	Clone the repository
https://github.com/ysoibelman-ai/ExpenseTracker.git
2-	Create and activate a virtual environment:
Type in terminal (Windows):
source/venv/Scripts/activate
3-	Install dependencies:
Type in terminal (Windows):
pip install -r requirements.txt

How to Use
There are 2 main ways to use the program. The first way is to just run python main.py from the terminal. This will activate the program which will guide you through adding expenses (it is through selecting different options and guiding instructions which are self-explanatory).
The second option is to add an expense or run a few functions directly through the terminal as follows:
1.	to add an expense type: python main.py add <title> <amount> <category>
2.	to see your report type: python main.py report note: if your total amount exceeds your monthly budget – a warning is also printed
3.	to see your expense list type: python main.py list <category> note: the category is optional

***to run test type in the terminal: python -m pytest -v


Settings:
This project uses environment variables
Copy settings template from secrets.env.example to create your on .env file. Make sure to use all the different fields and variables in the example file in your env and set your settings. Note that in the config file there are already set default values for all the fields in the env example file.

Packages:
	
| Package Name | Link | Why Used |
| :--- | :--- | :--- |
| **pytest** | https://docs.pytest.org/en/stable/getting-started.html | Used to run the tests on the program to make sure everything runs smoothly |
| **Python-dotenv** | https://pypi.org/project/python-dotenv/ | Used to read secret `.env` file and implement its content into the other parts of the project |
| **typer** | https://typer.tiangolo.com/tutorial/first-steps/ | Used to run the program directly through the CLI terminal |
| **questionary** | https://questionary.readthedocs.io/ | Used to create interactive input interface which include selecting different options and fancier print out text |
| **rich** | https://rich.readthedocs.io/en/stable/introduction.html <br> Table docs: https://rich.readthedocs.io/en/stable/tables.html | Used to create the table which the expenses are shown in the terminal |









