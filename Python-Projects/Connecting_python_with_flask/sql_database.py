import mysql.connector
from flask_app import app

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'python_with_mysql'

mysql = mysql.connector.connect(
  host=app.config['MYSQL_HOST'],
  user=app.config['MYSQL_USER'],
  password=app.config['MYSQL_PASSWORD'],
  database=app.config['MYSQL_DB']
)

cursor = mysql.cursor()

guess = input("Input ur Name? ")

cursor.execute("U * FROM pessoas")

cursor.execute("SELECT * FROM pessoas")
result = cursor.fetchall()

for row in result:
    print(row)