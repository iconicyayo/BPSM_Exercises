import MySQLdb, os
def mysql_table_to_dict2(host, user, password, database, table_name, key_column, value_column):
    # Python comment lines to remind me what this is doing 
    """
    Queries a MySQL table for two columns and pairs them into a Python dictionary.
    The 'key_column' values become dictionary keys, and all 'value_column' values for that key become the values.
    """
    connection = None
    # As always, use a try except structure for safety!
    try:
        connection = MySQLdb.connect(
            host=host,
            user=user,
            passwd=password,
            db=database
        )
        cursor = connection.cursor()
        # 1. Say which SQL table columns to use as key and value, using f strings
        query = f"SELECT {key_column}, GROUP_CONCAT(DISTINCT {value_column} SEPARATOR ', ')  FROM {table_name} GROUP BY {key_column}"
        cursor.execute(query)
        # 2. Get the results
        raw_data = cursor.fetchall()
        # 3. Convert the whole results set into a Python dictionary in a single step
        result_dict = dict(raw_data)
        return result_dict
    except MySQLdb.Error as e:
        print(f"Database error while creating dictionary: {e}")
        return {}
    finally:
        if connection and connection.open:
            cursor.close()
            connection.close()

if __name__ == "__main__":
    
  SQL_dict2 = mysql_table_to_dict2(
        host="127.0.0.1",
        user=os.environ["USER"],
        password='Yuffie123!!',
        database=os.environ["USER"],
	table_name="hit_table",
	key_column="sequence_id",
	value_column="accession"   
 )
