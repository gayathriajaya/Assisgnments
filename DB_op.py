# Import Statements
import sqlite3
import os
from pprint import pprint

# Global Variables
DB_PATH = '/Users/gajaya/Desktop/temp_data/test.db'


# Functions
# Create Table
def create_table(conn):
    query = '''CREATE TABLE COMPANY
           (ID INT PRIMARY KEY     NOT NULL,
           NAME           TEXT    NOT NULL,
           AGE            INT     NOT NULL,
           ADDRESS        CHAR(50),
           SALARY         REAL);'''
    conn.execute(query)
    print("Table created successfully");


# Insert
def insert_into_table(conn):
    queries = [
        "INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (1, 'Sohan', 32, 'Bengaluru', 20000.00 )",
        "INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (2, 'Siva', 25, 'Hyderabad', 15000.00 )",
        "INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (3, 'Rohan', 23, 'Pune', 20000.00 )",
        "INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (4, 'Rahul', 25, 'Chennai', 65000.00 )"
    ]
    for query in queries:
        conn.execute(query);
    conn.commit()
    print("Records created successfully");


# Select
def select_from_table(conn):
    cursor = conn.execute("SELECT id, name, address, salary  from COMPANY")

    for row in cursor:
        s = "ID={0}, Name={1}, Address={2}, Salary={3}\n".format(row[0], row[1], row[2], row[3])
        print(s)


# Select
def select_from_table1(conn):
    res = {}
    array = []
    cursor = conn.execute("SELECT id, name, address, salary  from COMPANY")

    for row in cursor:
        s = "ID={0}, Name={1}, Address={2}, Salary={3}\n".format(row[0], row[1], row[2], row[3])
        # print(s)
        ob_dict = {
            "ID": row[0],
            "Name": row[1],
            "Address": row[2],
            "Salary": row[3],
        }
        array.append(ob_dict)
    res['DB_data'] = array
    pprint(res)
    return res


# Update
def update_into_table(conn):
    conn.execute("UPDATE COMPANY set SALARY = 25000.00 where ID=1")
    conn.commit()
    print("Total number of rows updated :", conn.total_changes)


# Delete
def delete_from_table(conn):
    conn.execute("DELETE from COMPANY where ID=2;")
    conn.commit()
    print("Total number of rows deleted :", conn.total_changes)


# Main
if __name__ == '__main__':

    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)

    conn = sqlite3.connect(DB_PATH)

    create_table(conn)
    insert_into_table(conn)
    select_from_table(conn)
    update_into_table(conn)
    delete_from_table(conn)
    select_from_table(conn)
    conn.close()
