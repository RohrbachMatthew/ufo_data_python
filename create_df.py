# This file fetches data from MySQL database, queries all from ufo_sights table, returns rows and columns

import mysql.connector

def fetch_data():
    # Connect to the database, replace wih your own credentials
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='UFOData123',
        database='ufo',
        port='3307'
    )

    # Query the data
    query = 'Select * FROM ufo_sights'
    cursor = connection.cursor()
    cursor.execute(query)

    # Fetch all
    rows = cursor.fetchall()

    # Get column names from the cursor
    columns = [i[0] for i in cursor.description]
    '''
    Cursor.description is a list of tuples, each tuple describes a column.
    Gets column names at index 0 for each tuple.
    '''


    # Close connections
    cursor.close()
    connection.close()

    return rows, columns
