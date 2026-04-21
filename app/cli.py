import psycopg2
import os
from app.ingestion.csv_reader import read_csv_files
from app.validation.expense_schema import Expense
from app.db.insert_expense import insert_expense
from app.db.get_expenses import fetch_expenses
from tabulate import tabulate
from app.db.get_total import fetch_total
from app.db.connection import get_connection
from app.db.get_expenses_by_date import fetch_expenses_by_date
from app.db.create_table import create_table

def fetch_category_summary():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT category, SUM(amount)
        FROM expenses
        GROUP BY category
    """)
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows

def ingest():
    create_table()
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("TRUNCATE TABLE expenses RESTART IDENTITY")
    conn.commit()
    cursor.close()
    conn.close()
    rows = read_csv_files("data")
    for row in rows:
        try:
            expense = Expense(**row)
            insert_expense(expense)
            print("Inserted:", expense)
        except Exception as e:
            print("Invalid row:", row, "| Error:", e)

def data():
    rows = fetch_expenses()
    headers = ["ID", "Date", "Category", "Amount", "Description"]
    print(tabulate(rows, headers=headers, tablefmt="grid"))

def total():
    total_amount = fetch_total()
    print("Total Expenses:", total_amount)

def category():
    rows = fetch_category_summary()
    headers = ["Category", "Total Spent"]
    print(tabulate(rows, headers=headers, tablefmt="grid"))

def date_filter(date):
    rows = fetch_expenses_by_date(date)
    headers = ["ID", "Date", "Category", "Amount", "Description"]
    print(tabulate(rows, headers=headers, tablefmt="grid"))