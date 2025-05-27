import mysql.connector

__cnx = None

def get_sql_connection():
    print("Opening MySQL Connection")
    global __cnx

    if __cnx is None:
        try:
            __cnx = mysql.connector.connect(
                user='root',
                password='1234',
                database='grocery_store',
                host='localhost'  
            )
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return None

    return __cnx
