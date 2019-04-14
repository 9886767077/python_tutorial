import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="python12",
    database="mydb1"
)

mycursor = mydb.cursor()

sql = INSERT INTO customer (name, address, phone_no, data, pwd) VALUES ()