import pymysql
import os
from dotenv import load_dotenv

def import_database(table):
    # Load environment variables from .env file
    try:
        load_dotenv()
        host = os.environ.get("mysql_host")
        user = os.environ.get("mysql_user")
        password = os.environ.get("mysql_pass")
        database = os.environ.get("mysql_db")

        # Establish a database connection
        connection = pymysql.connect(
            host,
            user,
            password,
            database
        )

        # A cursor is an object that represents a DB cursor,
        # which is used to manage the context of a fetch operation.
        cursor = connection.cursor(pymysql.cursors.DictCursor)

        # Execute SQL query
        cursor.execute(f'SELECT * FROM {table}')

        # fetch all data as a list of dictionaries
        list = cursor.fetchall()

        
        cursor.close()

        # Closes the connection to the DB, make sure you ALWAYS do this
        connection.close()

        return list
    except:
        print(f'There was an error loading from {table} table. Please make sure the database is running...')
        empty_list = []
        return empty_list

def export_to_database(database_table, dict_list):
    # Load environment variables from .env file
    load_dotenv()
    host = os.environ.get("mysql_host")
    user = os.environ.get("mysql_user")
    password = os.environ.get("mysql_pass")
    database = os.environ.get("mysql_db")

    # Establish a database connection
    connection = pymysql.connect(
        host,
        user,
        password,
        database
    )

    # A cursor is an object that represents a DB cursor, which is used to manage the context of a fetch operation.
    cursor = connection.cursor()

    cursor.execute(f'delete from {database_table}')

    # Add code here to insert a new record
    # sql = "INSERT INTO person (first_name, last_name, age, email) VALUES (%s, %s, %s, %s)"
    # value = ('test', 'testson', '0', 'test@email.email')
    # cursor.execute(sql, value)

    for dict in dict_list:
        placeholders = ', '.join(['%s'] * len(dict))
        columns = ', '.join(dict.keys())
        sql = "INSERT INTO %s ( %s ) VALUES ( %s )" % (database_table, columns, placeholders)

        cursor.execute(sql, list(dict.values()))

    connection.commit()
    cursor.close()
    connection.close()