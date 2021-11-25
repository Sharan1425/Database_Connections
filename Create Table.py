import mysql.connector
myconnection = mysql.connector.connect(

    host = "localhost",
    user = "root",
    password = "knack@321",
    database = "sharan"
)

connection = myconnection.cursor()
table_name = input("please enter table : ")
connection.execute(f"create table {table_name} ( sno int(100) primary key, name varchar (50), age int (100), address varchar (200))")

print(f"{table_name} table is created successfully")

"New Feature added "