from mysql.connector import connect

db = connect(host="localhost", user="root", password="root", database="world")
handle = db.cursor()
handle.execute("select * from city where population>4000000")
city_names = handle.fetchall()
for city in city_names:
    print(city)
