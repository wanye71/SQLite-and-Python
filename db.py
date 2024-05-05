import sqlite3 as sql
import tkinter as tk

from tkinter import messagebox
from database_operations import DatabaseOperations
from db_app import DatabaseApp

# This line of code establishes a connection to an SQLite database named "customer.db"
conn = sql.connect('customer.db')


# The cursor object is obtained by calling the cursor() method on the connection object 'conn'
curs = conn.cursor()


db_ops = DatabaseOperations()
table_name = 'customers'

def CREATE_TABLE():
    db_ops.createTable(curs)


def main():
    # Create the main window
    root = tk.Tk()
    app = DatabaseApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

# This method commits the current transaction, making any changes permanent in the database
conn.commit()


# This method closes the connection to the database
conn.close()