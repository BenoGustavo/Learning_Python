#Endereco sendo criado duplicado

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
def create_funcionario(CPF, nome,email, telefone,logradouro, funcao ,cep, numero, bairro):
    
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

    #Caso não consiga criar funcionario, o endereco criado anteriormente é deletado e então finalizado a funcao

    try:
        sql = "INSERT INTO funcionario (CPF, nome, email, telefone ,funcao, id_endereco) VALUES (%s, %s, %s,%s,%s,%s)" #Criando o hospital, junto com o ID do respectivo endereco
        val = (CPF,nome, email,telefone,funcao,id_endereco[0],)
        cursor.execute(sql, val)
        mydb.commit()

    except:
            sql = "SELECT * FROM endereco ORDER BY id_endereco DESC LIMIT 1" #Selecionando informaçoes
            cursor.execute(sql)
            result = cursor.fetchone()

            sql = "DELETE FROM endereco WHERE id_endereco = %s"
            val = (result[0],) # o primeiro elemento de 'result' é o ID da última linha
            cursor.execute(sql, val)
            mydb.commit()

            raise "Falha ao cadastrar o funcionario" #Inserir um raise aqui

    finally:
        return cursor.lastrowid


#Lendo informacoes da tabela funcionario
def read_funcionario(id_funcionario):
    cursor = mydb.cursor()
    sql = "SELECT * FROM funcionario WHERE id_funcionario = %s" #Comando mysql || pegando informacoes do hospital com ID
    val = (id_funcionario,)
    cursor.execute(sql, val)
    result = cursor.fetchone()

    sql = "SELECT * FROM endereco WHERE id_endereco = %s" #Comando mysql || pegando informacoes do endereco hospital
    val = (result[6],)
    cursor.execute(sql, val)
    endereco = cursor.fetchone()
    
    #Retornando informacoes
    if result is None or endereco is None:
        return None
    return {'id': result[0], 'CPF': result[1], 'nome': result[2], 'email': result[3],"telefone":result[4],"funcao":result[5],'logradouro':endereco[1],'cep':endereco[2],'numero':endereco[3],'bairro':endereco[4]}

#Atuailizando informacoes funcionario
def update_funcionario(id_funcionario,CPF, nome,email, telefone,logradouro, funcao ,cep, numero, bairro):
    cursor = mydb.cursor()
    sql = "UPDATE funcionario SET CPF = %s, nome = %s, email = %s, telefone = %s, funcao = %s WHERE id_funcionario = %s" #Comando mysql || atulizando dados
    val = (CPF,nome, email,telefone,funcao,id_funcionario)
    cursor.execute(sql, val)
    mydb.commit()

    sql = "SELECT * FROM funcionario WHERE id_endereco = %s" #Selecionando ID endereco
    id = (id_funcionario,)
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
    
    update_endereco(logradouro, cep, numero, bairro,endereco[6]) #Funcao que atualiza o endereco

    return cursor.rowcount

#Deletando dados hospital
def delete_funcionario(id_funcionario):
    
    cursor = mydb.cursor()
    sql = "SELECT * FROM funcionario WHERE id_funcionario = %s" #Selecionando ID endereco
    id = (id_funcionario,)
    cursor.execute(sql, id)
    id_endereco = cursor.fetchone() #Armazenando ID endereco

    sql = "DELETE FROM endereco WHERE id_endereco = %s" #Deletando endereco || RECEBENDO ERRO POIS N POSSO DELETAR CHAVE ESTRANGEIRA
    val = (id_endereco[6],)
    cursor.execute(sql, val)
    
    sql = "DELETE FROM funcionario WHERE id_funcionario = %s" #Deletando informacoes do hospital
    val = (id_funcionario,)
    cursor.execute(sql, val)
    mydb.commit()
    

    
    return cursor.rowcount


#Utilizando

#Não funciona

#delete_funcionario(2) Não consigo deletar chave estrangeira

#Funcionando


#update_funcionario("1","12345","skibaripapa","skibaripapa@gmail.com","12340987","logradouro","pensar","987","678","doi")
#print(read_funcionario(1))
#create_funcionario("14758889961","gustavo","gustavo.gorges@faculdadecesusc.edu.br","32695585","rEvaristo_Guilherme_Dos_santos","atendlente","12344321","123","vargem")
