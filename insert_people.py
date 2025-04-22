import mysql.connector # type: ignore

people_db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "1234",
    database = "people_db"
)

cursor = people_db.cursor()
sql_statement = "INSERT INTO people(first_name, last_name, age) VALUES(%s,%s,%s)"
values = ("Charly", "Smith", 25)
cursor.execute(sql_statement,values)

people_db.commit()

print(f"New record added: {values}")
cursor.close()
people_db.close()