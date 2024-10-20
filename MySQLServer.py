import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL server (without specifying a database for now)
        connection = mysql.connector.connect(
            host='localhost',  # Use your MySQL server host, usually localhost
            user='root',  # Replace with your MySQL username
            password='Katawaligulu@1'  # Replace with your MySQL password
        )

        if connection.is_connected():
            print("Successfully connected to MySQL server")

            # Create a cursor object to interact with MySQL
            cursor = connection.cursor()

            # Check if the database already exists
            cursor.execute("SHOW DATABASES LIKE 'alx_book_store';")
            result = cursor.fetchone()
            
            if result:
                print("Database 'alx_book_store' already exists.")
            else:
                # Create the database if it doesn't exist
                cursor.execute("CREATE DATABASE alx_book_store")
                print("Database 'alx_book_store' created successfully!")

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
