
import os
import getpass
import MySQLdb

connection = None
cursor = None

try:
    connection = MySQLdb.connect(
        host="127.0.0.1",
        user=os.environ["USER"],
        passwd=getpass.getpass("MySQL password: "), 
        db=os.environ["USER"]     )

    # check the connection works
    cursor = connection.cursor()
    cursor.execute("SELECT VERSION()")
    db_version = cursor.fetchone()
    print(f"Database version: {db_version[0]}")

    # list the available tables
    cursor.execute("SHOW TABLES")
    print("+" * 60)
    for (table,) in cursor.fetchall():
        print(table)
    print("+" * 60)

    # check the structure of a specific table
    table_name = "hit_table"
    cursor.execute(f"DESCRIBE {table_name}")

    # retrieve the column information
    columns = cursor.fetchall()

    # display the table structure
    print(f"\nStructure for table: '{table_name}'")
    print("~" * 60)
    print(f"{'Field Name':<20} | {'Type':<15} | {'Null Allowed?':<12} | {'Key'}")
    print("~" * 60)

    # print each column
    for col in columns:
        print(f"{col[0]:<20} | {str(col[1]):<15} | {col[2]:<13} | {col[3]}")
    print("-" * 60)

except MySQLdb.Error as e:
    print(f"Error: {e}")

finally:
    if cursor is not None:
        cursor.close()
    if connection is not None:
        connection.close()
