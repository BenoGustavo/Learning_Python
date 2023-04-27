import mysql.connector

#Conectando ao schema

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="hospital_v2"
)

# CRUD HOSPITAL

def create_hospital(nome, email, telefone):
    cursor = mydb.cursor()
    sql = "INSERT INTO hospital (nome, email, telefone) VALUES (%s, %s, %s)"
    val = (nome, email,telefone)
    cursor.execute(sql, val)
    mydb.commit()
    return cursor.lastrowid

def read_hospital(id_hospital):
    cursor = mydb.cursor()
    sql = "SELECT * FROM hospital WHERE id_hospital = %s"
    val = (id_hospital,)
    cursor.execute(sql, val)
    result = cursor.fetchone()
    if result is None:
        return None
    return {'id': result[0], 'name': result[1], 'telefone': result[2], 'email': result[3]}

def update_hospital(id_hospital, nome, email, telefone):
    cursor = mydb.cursor()
    sql = "UPDATE hospital SET nome = %s, email = %s, telefone = %i WHERE id = %s"
    val = (nome, email, telefone ,id_hospital)
    cursor.execute(sql, val)
    mydb.commit()
    return cursor.rowcount

def delete_hospital(id_hospital):
    cursor = mydb.cursor()
    sql = "DELETE FROM hospital WHERE id_hospital = %s"
    val = (id_hospital,)
    cursor.execute(sql, val)
    mydb.commit()
    return cursor.rowcount

#CRUD ENDEREÇO


def create_endereco(logradouro, cep, numero, bairro):
    cursor = mydb.cursor()
    sql = "INSERT INTO endereco (logradouro, cep, numero, bairro) VALUES (%s, %s, %s, %s)"
    val = (logradouro, cep, numero, bairro)
    cursor.execute(sql, val)
    mydb.commit()
    return cursor.lastrowid

def read_endereco(id_endereco):
    cursor = mydb.cursor()
    sql = "SELECT * FROM endereco WHERE id_endereco = %s"
    val = (id_endereco,)
    cursor.execute(sql, val)
    result = cursor.fetchone()
    if result is None:
        return None
    return {'id': result[0], 'logradouro': result[1], 'cep': result[2], 'numero': result[3], 'bairro': result[4]}

def update_endereco(id_endereco, logradouro, cep, numero, bairro):
    cursor = mydb.cursor()
    sql = "UPDATE endereco SET logradouro = %s, cep = %s, numero = %s, bairro = %s WHERE id = %s"
    val = (logradouro, cep, numero, bairro,id_endereco)
    cursor.execute(sql, val)
    mydb.commit()
    return cursor.rowcount

def delete_endereco(id_endereco):
    cursor = mydb.cursor()
    sql = "DELETE FROM endereco WHERE id_endereco = %s"
    val = (id_endereco,)
    cursor.execute(sql, val)
    mydb.commit()
    return cursor.rowcount


#Utilizando


create_hospital("exemplo de hospital","hospital@gmail.com","2345678")
