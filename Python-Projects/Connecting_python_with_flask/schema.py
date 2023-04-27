import mysql.connector
from app import app

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'python_flask_with_mysql'

mysql_connection = mysql.connector.connect(
  host=app.config['MYSQL_HOST'],
  user=app.config['MYSQL_USER'],
  password=app.config['MYSQL_PASSWORD'],
  database=app.config['MYSQL_DB']
)

cursor = mysql_connection.cursor()

name = input("What's ur first name?")

last_name = input("What's ur last name?")

age = input("How old you are?")

consulta = f"INSERT INTO pessoa (nome,sobrenome,idade) VALUES ({name},{last_name},{age})"

mysql_connection.commit()

cursor.execute(f"SELECT * FROM pessoa")
resultados = cursor.fetchall()

for row in resultados:
    print(row)
