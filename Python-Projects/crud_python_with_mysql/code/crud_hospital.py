import mysql.connector

#Conectando ao schema

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="hospital_v2"
)

# CRUD HOSPITAL

#Criando hospital
def create_hospital(nome, email, telefone,logradouro, cep, numero, bairro):
    
    #Criando endereco para o hospital
    def create_endereco(logradouro, cep, numero, bairro):
        
        cursor = mydb.cursor()
        sql = "INSERT INTO endereco (logradouro, cep, numero, bairro) VALUES (%s, %s, %s, %s)" #Comando mysql
        val = (logradouro, cep, numero, bairro)
        cursor.execute(sql, val)
        mydb.commit()
        return cursor.lastrowid
    
    create_endereco(logradouro, cep, numero, bairro) #Chamando a funcao que cria o endereco para o hospital

    cursor = mydb.cursor()

    sql = "SELECT * FROM endereco ORDER BY id_endereco DESC LIMIT 1" #Selecionando o ID do endereco
    cursor.execute(sql)
    id_endereco = cursor.fetchone()

    sql = "INSERT INTO hospital (nome, email, telefone, id_endereco) VALUES (%s, %s, %s,%s)" #Criando o hospital, junto com o ID do respectivo endereco
    val = (nome, email,telefone,id_endereco[0],)
    cursor.execute(sql, val)
    mydb.commit()
    return cursor.lastrowid


#Lendo informacoes da tabela hospital
def read_hospital(id_hospital):
    cursor = mydb.cursor()
    sql = "SELECT * FROM hospital WHERE id_hospital = %s" #Comando mysql || pegando informacoes do hospital com ID
    val = (id_hospital,)
    cursor.execute(sql, val)
    result = cursor.fetchone()

    sql = "SELECT * FROM endereco WHERE id_endereco = %s" #Comando mysql || pegando informacoes do endereco hospital
    val = (result[4],)
    cursor.execute(sql, val)
    endereco = cursor.fetchone()
    
    #Retornando informacoes
    if result is None or endereco is None:
        return None
    return {'id': result[0], 'name': result[1], 'telefone': result[2], 'email': result[3],'logradouro':endereco[1],'cep':endereco[2],'numero':endereco[3],'bairro':endereco[4]}

#Atuailizando informacoes hospital
def update_hospital(id_hospital,nome, email, telefone,logradouro, cep, numero, bairro):
    cursor = mydb.cursor()
    sql = "UPDATE hospital SET nome = %s, email = %s, telefone = %s WHERE id_hospital = %s" #Comando mysql || atulizando dados
    val = (nome, email, telefone ,id_hospital)
    cursor.execute(sql, val)
    mydb.commit()

    sql = "SELECT * FROM hospital WHERE id_hospital = %s" #Selecionando ID endereco
    id = (id_hospital,)
    cursor.execute(sql, id)
    endereco = cursor.fetchone() #Armazenando ID endereco

    #Atuailizando informacoes endereco
    def update_endereco(logradouro, cep, numero, bairro,endereco):

        #Comando mysql || Atuailizar informacoes endereco do hospital
        sql = "UPDATE endereco SET logradouro = %s, cep = %s, numero = %s, bairro = %s WHERE id_endereco = %s"
        val = (logradouro, cep, numero, bairro,endereco)
        cursor.execute(sql, val)
        mydb.commit()
        return cursor.rowcount
    
    update_endereco(logradouro, cep, numero, bairro,endereco[4]) #Funcao que atualiza o endereco

    return cursor.rowcount

#Deletando dados hospital
def delete_hospital(id_hospital):
    
    cursor = mydb.cursor()
    sql = "SELECT * FROM hospital WHERE id_hospital = %s" #Selecionando ID endereco
    id = (id_hospital,)
    cursor.execute(sql, id)
    id_endereco = cursor.fetchone() #Armazenando ID endereco

    sql = "DELETE FROM endereco WHERE id_endereco = %s" #Deletando endereco || RECEBENDO ERRO POIS N POSSO DELETAR CHAVE ESTRANGEIRA
    val = (id_endereco[4],)
    cursor.execute(sql, val)
    
    cursor = mydb.cursor()
    sql = "DELETE FROM hospital WHERE id_hospital = %s" #Deletando informacoes do hospital
    val = (id_hospital,)
    cursor.execute(sql, val)
    mydb.commit()
    

    
    return cursor.rowcount


#Utilizando

create_hospital("TESTE","TESTE@GMAIL.COM","321","LOGRADOURO","768","876789","BAIRRO")
#update_hospital("5","nome","string","123","string","123","123","string")
