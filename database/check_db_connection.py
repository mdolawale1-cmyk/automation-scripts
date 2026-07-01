"""Checks database connectivity and reports connection status."""

import mysql.connector
from mysql.connector import Error

def check_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",       # Replace with your DB host
            user="root",            # Replace with your DB username
            password="password",    # Replace with your DB password
            database="test_db"      # Replace with your DB name
        )
        if connection.is_connected():
            print("Database connection successful ✅")
    except Error as e:
        print(f"Database connection failed ❌ — {e}")
    finally:
        if 'connection' in locals() and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    check_connection()
