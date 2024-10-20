import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL server (without specifying a database for now)
        connection = mysql.connector.connect(
            host='localhost',  # Use your MySQL server host, usually localhost
            user='your_user',  # Replace with your MySQL username
            password='your_password'  # Replace with your MySQL password
        )

        if connection.is_connected():
            print("Successfully connected to MySQL server")

            # Create a cursor object to interact with MySQL
            cursor = connection.cursor()

            # Use CREATE DATABASE IF NOT EXISTS to avoid error if the database already exists
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully (if it didn't already exist).")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    
    finally:
        # Close cursor and connection
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

# Run the function to create the database
if __name__ == "__main__":
    create_database()
