import mysql.connector

# Use YOUR CREDENTIALS here
db = mysql.connector.connect(
    host = "localhost",
    user="pip",
    password="popo",
)

cursor = db.cursor()

mycursor.execute("CREATE DATABASE testdb")