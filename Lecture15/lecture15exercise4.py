
#!/usr/bin/env python3

# import os to access the current linux username
import os

# import MySQLdb to connect python to a mysql database
import MySQLdb


# define a function to retrieve the available database tables
# cursor allows the function to execute sql commands
def choose_table(cursor):

    # execute() sends an sql command to the database
    # SHOW TABLES retrieves the names of available tables
    cursor.execute("SHOW TABLES")

    # fetchall() retrieves all rows returned by the sql query
    tables = cursor.fetchall()

    # display a heading before listing the tables
    print("available tables:")

    # for loops through each row of the returned results
    # (table,) extracts the table name from each single-column row
    for (table,) in tables:

        # print() displays the current table name
        print(table)

    # input() asks the user to enter a table name
    table_name = input("enter table name: ")

    # in checks whether the selected table exists in the results
    # (table_name,) matches the tuple format returned by fetchall()
    if (table_name,) in tables:

        # display confirmation of the selected table
        print("selected table:", table_name)

        # return sends the selected table name to the calling code
        return table_name

    # else runs if the selected table is not found
    else:

        # display an error message
        print("table not found")

        # return None to indicate that no valid table was selected
        return None


# define a second function to display the structure of a selected table
# cursor provides database access and table_name identifies the table
def show_structure(cursor, table_name):

    # execute() sends the DESCRIBE command to mysql
    # DESCRIBE retrieves information about a table's columns
    cursor.execute("DESCRIBE " + table_name)

    # fetchall() retrieves the information returned by DESCRIBE
    columns = cursor.fetchall()

    # display the name of the selected table
    print("structure of table:", table_name)

    # loop through each row of column information
    for column in columns:

        # display information about the current column
        print(column)


# input() asks the user to enter the mysql password
# the entered password is stored temporarily in a variable
password = input("enter mysql password: ")

# try attempts the following database operations
# except handles mysql errors if the connection or query fails
try:

    # connect() establishes a connection to the mysql database
    # host specifies the database server
    # os.environ["USER"] retrieves the current linux username
    # passwd supplies the entered password
    # db specifies the user's exercises database
    connection = MySQLdb.connect(
        host="127.0.0.1",
        user=os.environ["USER"],
        passwd=password,
        db=os.environ["USER"] + "_exercises"
    )

    # display confirmation that the connection was successful
    print("connected to mysql database")

    # cursor() creates an object used to execute sql commands
    cursor = connection.cursor()

    # call choose_table() and store the returned table name
    selected_table = choose_table(cursor)

    # != checks whether selected_table is different from None
    # only continue if a valid table name was selected
    if selected_table != None:

        # call show_structure() to display the table information
        show_structure(cursor, selected_table)

    # close() releases the database cursor
    cursor.close()

    # close() disconnects from mysql
    connection.close()

    # confirm that the database connection has closed
    print("database connection closed")

# except catches mysql errors such as an incorrect password
# as e stores the error information for display
except MySQLdb.Error as e:

    # display the database error
    print("database error:", e)


## example results:
## enter mysql password: [password entered by user]
## connected to mysql database
## available tables:
## blasthits
## enter table name: blasthits
## selected table: blasthits
## structure of table: blasthits
## column information displayed here
## database connection closed
##
## actual table names and column information depend on the database

## logic: import os and MySQLdb; define a function to retrieve and display available tables; execute show tables and retrieve results using fetchall(); loop through table names using for; obtain user selection using input(); check whether the selected table exists; return the table name or none; define a second function to display table structure using describe; connect to mysql and create a cursor; call both functions; display table information; close cursor and connection; handle database errors using try and except
