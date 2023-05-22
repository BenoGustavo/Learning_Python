import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="python_with_mysql"
)

def create_pessoas(nome, idade, altura):
    cursor = mydb.cursor()
    sql = "INSERT INTO pessoas (Nome,Idade,Altura) VALUES (%s, %s, %s)"
    val = (nome,idade,altura,)
    cursor.execute(sql,val)
    mydb.commit()
    return cursor.lastrowid

def read_pessoas(id_pessoa):
    cursor = mydb.cursor()
    sql = "SELECT * FROM pessoas WHERE ID = %s"
    val = (id_pessoa,)
    cursor.execute(sql, val)
    result = cursor.fetchone()
    if result is None:
        return None
    return {'ID': result[0],'nome': result[1], 'idade': result[2], 'altura': result[3]}

create_pessoas("Gustavo","19","1.80")

print(read_pessoas(7))

