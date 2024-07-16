import mysql.connector
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='NsINFINITY6617'
)
cursor = connection.cursor()
cursor.execute("CREATE DATABASE KLAUSE")

print("All done")
