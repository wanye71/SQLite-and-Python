import tkinter as tk
from tkinter import messagebox
import sqlite3
from database_operations import DatabaseOperations

class DatabaseApp:
    def __init__(self, master):
        self.master = master
        master.title("Database Operations")

        # Create buttons for each operation
        self.insert_button = tk.Button(master, text="Insert Rows", command=self.insert_rows)
        self.insert_button.pack()

        self.select_button = tk.Button(master, text="Select Row Data", command=self.select_row_data)
        self.select_button.pack()

        self.delete_button = tk.Button(master, text="Delete All Rows", command=self.delete_all_rows)
        self.delete_button.pack()

        # Initialize database connection and cursor
        self.conn = sqlite3.connect('customer.db')
        self.curs = self.conn.cursor()
        self.table_name = 'customers'
        self.db_ops = DatabaseOperations()

    def insert_rows(self):
        # Call the INSERT_ROWS function
        insert_records = [('Wayne', 'Hatter', 'wayne@wayne.com'), 
                          ('Jack', 'Frost', 'jack@jack.com'), 
                          ('Nick', 'Jones', 'nick@nick.com')]
        self.db_ops.insertData(self.curs, insert_records)
        self.conn.commit()
        messagebox.showinfo("Info", "Insert Rows function executed")

    def select_row_data(self):
        # Call the SELECT_ROW_DATA function
        self.curs.execute("SELECT * FROM customers")
        rows = self.curs.fetchall()
        print(rows)  # Print the selected rows in the console
        messagebox.showinfo("Info", "Select Row Data function executed")

    def delete_all_rows(self):
        # Call the DELETE_ALL_ROWS function
        self.curs.execute('DELETE FROM {}'.format(self.table_name))
        self.conn.commit()
        messagebox.showinfo("Info", "Delete All Rows function executed")

def main():
    # Create the main window
    root = tk.Tk()
    app = DatabaseApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
