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
    sql = "INSERT INTO hospital (nome, email, telefone) VALUES (%s, %s, %i)"
    val = (nome, email,telefone,)
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
    sql = "INSERT INTO endereco (logradouro, cep, numero, bairro) VALUES (%s, %i, %i, %s)"
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
    sql = "UPDATE endereco SET logradouro = %s, cep = %i, numero = %i, bairro = %s WHERE id = %s"
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

# criando endereco

endereco_id = create_endereco("logradouro", "123", "456","bairro")
print("Created endereco with ID:", endereco_id)

# criando hospital

hospital_id = create_hospital("Hospital teste", "teste@gmail.com", "99999999")
print("Created Hospital with ID:", hospital_id)

# ler hospital

hospital = read_hospital(hospital_id)
if hospital is not None:
    print("Read Hospital:", hospital)
else:
    print("Hospital not found")

# att hospital

updated_count = update_hospital(hospital_id, "Hospital teste com outro nome", "testedeupdate@gmail.com","111111111")
print("Updated", updated_count, "Hospital")

# ler hospital

hospital = read_hospital(hospital_id)
if hospital is not None:
    print("Read Hospital:", hospital)
else:
    print("Hospital not found")
