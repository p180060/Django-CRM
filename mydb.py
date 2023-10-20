import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'malik',
    passwd = 'Sher#951357'
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE elderco")

print("ALL DONE")