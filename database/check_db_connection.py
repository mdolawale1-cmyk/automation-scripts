import mysql.connector
from mysql.connector import Error

def check_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",       # replace with your DB host
            user="root",            # replace with your DB username
            password="password",    # replace with your DB password
            database="testdb"       # replace with your DB name
        )
        if connection.is_connected():
            print("✅ Database connection successful!")
            cursor = connection.cursor()
            cursor.execute("SELECT DATABASE();")
            record = cursor.fetchone()
            print("Connected to database:", record)
    except Error as e:
        print("❌ Error while connecting to database:", e)
    finally:
        if 'connection' in locals() and connection.is_connected():
            connection.close()
            print("🔒 Database connection closed.")

if __name__ == "__main__":
    check_connection()
