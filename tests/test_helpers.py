from helpers import total, total_category, total_by_category
from expense import *

def test_total_empty():
    assert total([]) == 0

def test_total_two_expenses():
    expenses = [ (Expense ("10","Milk","food","1000")),(Expense ("10","Meat","food","2000"))]
    assert total(expenses) == 3000

def test_total_by_category():
    expenses = [ (Expense ("10","Milk","food","1000")),(Expense ("10","Meat","food","2000")),
                (Expense ("10","Phone","other","1000")),(Expense ("10","Sneakers","other","500"))]
    assert total_by_category(expenses) == {"food":3000,"other":1500}

def test_total_category():
    expenses = [ (Expense ("10","Milk","food","1000")),(Expense ("10","Meat","food","2000")),
                 (Expense ("10","Phone","other","1000")),(Expense ("10","Sneakers","other","500"))
                ]
    assert total_category(expenses,"other") == 1500