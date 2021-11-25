import mysql.connector

from InsertDate import Dbconnection

myconnection  = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password ="knack@321",
    database = "sharan"
)

Dbconnection = myconnection.cursor()

sql_query = "delete from my_info where sno = 4";    

Dbconnection.execute(sql_query)

myconnection.commit()

print("Record has been deleted successfully")


"New line added..."