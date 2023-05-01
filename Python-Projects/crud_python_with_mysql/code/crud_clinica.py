import mysql.connector

#Conectando ao schema

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="hospital_v2"
)

# CRUD clinica

#Criando clinica
def create_clinica(especialidade,id_hospital):

    cursor = mydb.cursor()

    sql = "SELECT COUNT(*) FROM hospital" #Comando mysql || verificando existencia de um hospital valido
    cursor.execute(sql,)
    result = cursor.fetchone()

    if result == 0:
        return "Primeiro crie uma hospital para vincular sua clinica"
    
    sql = "SELECT * FROM hospital WHERE id_hospital = %s" #Selecionando hospital
    id = (id_hospital,)
    cursor.execute(sql, id)
    verifica_hospital = cursor.fetchone() #Armazenando

    if verifica_hospital == None:
        return "Hospital invalido"

    sql = "INSERT INTO clinica (especialidade, id_hospital) VALUES (%s, %s)" #Criando o clinica, junto com o ID do respectivo endereco
    val = (especialidade, id_hospital)
    cursor.execute(sql, val)
    mydb.commit()
    return cursor.lastrowid


#Lendo informacoes da tabela clinica
def read_clinica(id_clinica):
    cursor = mydb.cursor()
    sql = "SELECT * FROM clinica WHERE id_clinica = %s" #Comando mysql || pegando informacoes do clinica com ID
    val = (id_clinica,)
    cursor.execute(sql, val)
    result = cursor.fetchone()

    sql = "SELECT * FROM hospital WHERE id_hospital = %s" #Comando mysql || recebendo info hospital vinculado
    val = (result[2],)
    cursor.execute(sql, val,)
    hospital_nome = cursor.fetchone()   
    
    #Retornando informacoes
    if result is None or hospital_nome is None:
        return None
    return {'id': result[0], 'especialidade': result[1], 'hospital vinculado': hospital_nome[1]}

#Atuailizando informacoes clinica
def update_clinica(id_clinica,especialidade,id_hospital):

    cursor = mydb.cursor()
    sql = "SELECT * FROM hospital WHERE id_hospital = %s" #Selecionando hospital
    id = (id_hospital,)
    cursor.execute(sql, id)
    verifica_hospital = cursor.fetchone() #Armazenando

    if verifica_hospital == None:
        return "Hospital invalido"

    sql = "UPDATE clinica SET especialidade = %s, id_hospital = %s WHERE id_clinica = %s" #Comando mysql || atulizando dados
    val = (especialidade,id_hospital,id_clinica)
    cursor.execute(sql, val)
    mydb.commit()

    sql = "SELECT * FROM clinica WHERE id_clinica = %s" #Selecionando ID endereco
    id = (id_clinica,)
    cursor.execute(sql, id)
    endereco = cursor.fetchone() #Armazenando ID endereco

    return cursor.rowcount

#Deletando dados clinica
def delete_clinica(id_clinica):
    
    cursor = mydb.cursor()
    sql = "SELECT * FROM clinica WHERE id_clinica = %s" #Selecionando ID endereco
    id = (id_clinica,)
    cursor.execute(sql, id)
    id_endereco = cursor.fetchone() #Armazenando ID endereco

    sql = "DELETE FROM endereco WHERE id_endereco = %s" #Deletando endereco || RECEBENDO ERRO POIS N POSSO DELETAR CHAVE ESTRANGEIRA
    val = (id_endereco[4],)
    cursor.execute(sql, val)
    
    cursor = mydb.cursor()
    sql = "DELETE FROM clinica WHERE id_clinica = %s" #Deletando informacoes do clinica
    val = (id_clinica,)
    cursor.execute(sql, val)
    mydb.commit()
    

    
    return cursor.rowcount


#Utilizando

print(create_clinica("&¨$%#¨&$%&#¨%$#*¨$#$%¨#%$*¨%*&#$¨*$&¨#*$&#¨$*&¨$*&#¨*&$#*&$*#&*$&#&$&#¨*$&#¨*$¨*&$&¨#&$#&$#&*$&¨&#$&$&#¨$&#¨*$¨*#$*#$&¨*#¨¨$*¨#$¨*#&¨*$&¨#*&$¨*#¨&$¨#*$&¨&#¨$*#¨&¨$*¨$#$#$&#*$¨*#&¨$*#¨&$¨#&$¨#&$&#*$&#**$&¨*$#*&$#*&$#$&#¨$#&¨$&#$*#*&$¨#&$*&#$#&$#&$&#$&*#&$*&$&#$*&#$#&$#&*$&#*&$¨#%¨%&¨#%&%*&#%&#*%&¨%&%¨¨%#(*$@&*($&@(*&$(*@&$*(&@&%¨¨@&$&¨@&$¨*¨#*&(#*","1"))