import mysql.connector

def connect_db():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Aju.magic13",
            database="voting_system"
        )
        return connection
    except mysql.connector.Error as e:
        print(f"Database connection failed: {e}")
        return None
