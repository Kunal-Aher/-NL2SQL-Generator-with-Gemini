# # create database connection
import mysql.connector
from mysql.connector import Error

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Aher@123",
    database="classicmodels",
    port="3306"
)
print("Connection successful")
cursor = connection.cursor()
cursor.execute("SHOW TABLES")
tables = cursor.fetchall()
print("Tables:")
for t in tables:
    print(t)
# create table students
cursor.execute("create table if not exists students (id int auto_increment primary key, name varchar(255), age int, grade varchar(255))")
print("Table students created successfully")

cursor.execute("SHOW TABLES")
tables = cursor.fetchall()
print("Tables:")
for t in tables:
    print(t)

# print("Table students created successfully")
#insert data into students table
cursor.execute("INSERT INTO students (name, age, grade) VALUES (%s, %s, %s)", ("John Doe", 20, "A"))
cursor.execute("INSERT INTO students (name, age, grade) VALUES (%s, %s, %s)", ("Jane Doe", 22, "B"))
cursor.execute("INSERT INTO students (name, age, grade) VALUES (%s, %s, %s)", ("Jim Doe", 21, "C"))
cursor.execute("INSERT INTO students (name, age, grade) VALUES (%s, %s, %s)", ("Jack Doe", 23, "D"))
cursor.execute("INSERT INTO students (name, age, grade) VALUES (%s, %s, %s)", ("Jill Doe", 24, "E"))
cursor.execute("INSERT INTO students (name, age, grade) VALUES (%s, %s, %s)", ("Joe Doe", 25, "F"))
cursor.execute("INSERT INTO students (name, age, grade) VALUES (%s, %s, %s)", ("Judy Doe", 26, "G"))
cursor.execute("INSERT INTO students (name, age, grade) VALUES (%s, %s, %s)", ("Jackie Doe", 27, "H"))
cursor.execute("INSERT INTO students (name, age, grade) VALUES (%s, %s, %s)", ("Jasmine Doe", 28, "I"))
cursor.execute("INSERT INTO students (name, age, grade) VALUES (%s, %s, %s)", ("Jasper Doe", 29, "J"))
cursor.execute("INSERT INTO students (name, age, grade) VALUES (%s, %s, %s)", ("Jett Doe", 30, "K"))
cursor.execute("INSERT INTO students (name, age, grade) VALUES (%s, %s, %s)", ("Juno Doe", 31, "L"))
cursor.execute("INSERT INTO students (name, age, grade) VALUES (%s, %s, %s)", ("Jade Doe", 32, "M"))
cursor.execute("INSERT INTO students (name, age, grade) VALUES (%s, %s, %s)", ("Jade Doe", 32, "M"))
cursor.execute("INSERT INTO students (name, age, grade) VALUES (%s, %s, %s)", ("Jade Doe", 32, "M"))

cursor.execute("Select * from students")
rows = cursor.fetchall()
for row in rows:
    print(row)
# commit the changes


connection.commit()
cursor.close()
connection.close()
print("Data inserted successfully")
