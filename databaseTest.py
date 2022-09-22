import mysql.connector

conn = mysql.connector.connect(username='root', password='',host='localhost',database='min_1',port=3306)
cursor = conn.cursor()

cursor.execute("show databases")

data = cursor.fetchall()

print(data)

conn.close()