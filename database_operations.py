import sqlite3 as sql


class DatabaseOperations:
    def createTable(self, cursor):
        try:
            # Attempt to execute the SQL statement to create the table
            cursor.execute('''CREATE TABLE customers (
                            first_name text,
                            last_name text,
                            email text
                        )''')
            # If the table creation is successful and no exception is raised,
            # print a message indicating that the table was created
            print("Table 'customers' created successfully.")

        except sql.OperationalError as e:
            # If an OperationalError exception is raised, it means the table already exists
            # Print a message indicating that the table already exists
            print("Table 'customers' already exists.")

    def insertData(self, cursor, insert_records):
        try:
            # Attempt to execute the SQL statement to insert a record into the 'customers' table
            cursor.executemany('''INSERT INTO customers VALUES (?, ?, ?)''', (insert_records))
            # If the record insertion is successful and no exception is raised,
            # print a message indicating that the record was inserted
            print("Record inserted successfully.")

        except sql.IntegrityError as e:
            # If an IntegrityError exception is raised, it means the record already exists
            # Print a message indicating that the record already exists
            print("Record already exists.")
