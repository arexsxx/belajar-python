import mysql.connector

db = mysql.connector.connect()
host = 'localhost',
user = 'root',
password = '',
database = 'alpro'

myCursor = db.cursor()


sql = "INSERT INTO tb_matkul (b_indo, android, tbo) VALUES (%s,%s,%s)"
data = [100,80,90]
myCursor.execute(sql,data)
db.commit()

