import mysql.connector

myconnection  = mysql.connector.connect(
    host="localhost",
    user="root",
    password = "knack@321",
    database="sharan"
)

Dbconnection = myconnection.cursor()
try:
    sql_query1 = "insert into my_info values(10,'Sai',25,'Atp')"
    Dbconnection.execute(sql_query1)
    myconnection.commit()
except:
    print("Data is not inserted")

finally:

    print("Record is inserted successfully")
    myconnection.close()
