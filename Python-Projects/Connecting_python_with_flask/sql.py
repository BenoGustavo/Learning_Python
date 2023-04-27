import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="python_with_mysql"
)

def create_pessoas(nome, idade, altura,id):
    cursor = mydb.cursor()
    sql = "INSERT INTO pessoas (Nome,Idade,Altura,ID) VALUES (%s, %i, %f,%i)"
    val = (nome,idade,altura,id)
    cursor.execute(sql, val)
    mydb.commit()
    return cursor.lastrowid

def read_pessoas(id_pessoa):
    cursor = mydb.cursor()
    sql = "SELECT * FROM pessoas WHERE ID = %i"
    val = (id_pessoa,)
    cursor.execute(sql, val)
    result = cursor.fetchone()
    if result is None:
        return None
    return {'nome': result[0], 'idade': result[1], 'altura': result[2], 'ID': result[3]}

create_pessoas("Gustavo",19,1.80,1)

