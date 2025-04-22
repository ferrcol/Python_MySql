import mysql.connector # type: ignore

people_db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "1234",
    database = "people_db"
)

cursor = people_db.cursor()
cursor.execute("SELECT * FROM people")

result = cursor.fetchall()
for person in result:
    print(person)

cursor.close()
people_db.close()