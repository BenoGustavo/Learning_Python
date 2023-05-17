# Endereco sendo criado duplicado

import mysql.connector

# Conectando ao schema

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="hospital_v2"
)

# CRUD HOSPITAL

# Criando hospital


def show_all_id_from_table(table_name):
    cursor = mydb.cursor()

    cursor.execute(f"SELECT id_{table_name} FROM {table_name}")
    result = cursor.fetchall()
    return result


def show_all_name_from_table(table_name):
    cursor = mydb.cursor()

    cursor.execute(f"SELECT nome FROM {table_name}")
    result = cursor.fetchall()
    return result


def create_medicos(CPF, nome, email, telefone, logradouro, especialidade, cep, numero, bairro):

    # Criando endereco para o hospital
    def create_endereco(logradouro, cep, numero, bairro):

        cursor = mydb.cursor()
        # Comando mysql
        sql = "INSERT INTO endereco (logradouro, cep, numero, bairro) VALUES (%s, %s, %s, %s)"
        val = (logradouro, cep, numero, bairro)
        cursor.execute(sql, val)
        mydb.commit()
        return cursor.lastrowid

    # Chamando a funcao que cria o endereco para o hospital
    create_endereco(logradouro, cep, numero, bairro)

    cursor = mydb.cursor()

    # Selecionando o ID do endereco
    sql = "SELECT * FROM endereco ORDER BY id_endereco DESC LIMIT 1"
    cursor.execute(sql)
    id_endereco = cursor.fetchone()

    # Caso não consiga criar medicos, o endereco criado anteriormente é deletado e então finalizado a funcao

    try:
        # Criando o hospital, junto com o ID do respectivo endereco
        sql = "INSERT INTO medicos (CPF, nome, email, telefone ,especialidade, id_endereco) VALUES (%s, %s, %s,%s,%s,%s)"
        val = (CPF, nome, email, telefone, especialidade, id_endereco[0],)
        cursor.execute(sql, val)
        mydb.commit()

    except Exception as error:

        # Selecionando informaçoes
        sql = "SELECT * FROM endereco ORDER BY id_endereco DESC LIMIT 1"
        cursor.execute(sql)
        result = cursor.fetchone()

        sql = "DELETE FROM endereco WHERE id_endereco = %s"
        # o primeiro elemento de 'result' é o ID da última linha
        val = (result[0],)
        cursor.execute(sql, val)
        mydb.commit()

        print("Ocorreu um erro:", error)
        input("\n...")

    finally:
        return cursor.lastrowid


# Lendo informacoes da tabela medicos
def read_medicos(id_medicos):
    cursor = mydb.cursor()
    # Comando mysql || pegando informacoes do hospital com ID
    sql = "SELECT * FROM medicos WHERE id_medicos = %s"
    val = (id_medicos,)
    cursor.execute(sql, val)
    result = cursor.fetchone()

    # Comando mysql || pegando informacoes do endereco hospital
    sql = "SELECT * FROM endereco WHERE id_endereco = %s"
    val = (result[6],)
    cursor.execute(sql, val)
    endereco = cursor.fetchone()

    # Retornando informacoes
    if result is None or endereco is None:
        return None
    return {'id': result[0], 'CPF': result[1], 'nome': result[2], 'email': result[3], "telefone": result[4], "especialidade": result[5], 'logradouro': endereco[1], 'cep': endereco[2], 'numero': endereco[3], 'bairro': endereco[4]}

# Atuailizando informacoes medicos


def update_medicos(id_medicos, CPF=None, nome=None, email=None, telefone=None, logradouro=None, especialidade=None, cep=None, numero=None, bairro=None):
    cursor = mydb.cursor()

    # Comando mysql || atulizando dados
    sql = "UPDATE medicos SET CPF = %s, nome = %s, email = %s, telefone = %s, especialidade = %s WHERE id_medicos = %s"
    val = (CPF, nome, email, telefone, especialidade, id_medicos)
    cursor.execute(sql, val)
    mydb.commit()

    sql = "SELECT * FROM medicos WHERE id_medicos = %s"  # Selecionando ID endereco
    id = (id_medicos,)
    cursor.execute(sql, id)
    endereco = cursor.fetchone()  # Armazenando ID endereco

    # Atuailizando informacoes endereco
    def update_endereco(logradouro, cep, numero, bairro, endereco):

        # Comando mysql || Atuailizar informacoes endereco do hospital
        sql = "UPDATE endereco SET logradouro = %s, cep = %s, numero = %s, bairro = %s WHERE id_endereco = %s"
        val = (logradouro, cep, numero, bairro, endereco)
        cursor.execute(sql, val)
        mydb.commit()
        return cursor.rowcount

    # Funcao que atualiza o endereco
    update_endereco(logradouro, cep, numero, bairro, endereco[6])

    return cursor.rowcount

# Deletando dados hospital


def delete_medicos(id_medicos):

    cursor = mydb.cursor()
    sql = "SELECT * FROM medicos WHERE id_medicos = %s"  # Selecionando ID endereco
    id = (id_medicos,)
    cursor.execute(sql, id)
    id_endereco = cursor.fetchone()  # Armazenando ID endereco

    # Deletando informacoes do medicos
    sql = "DELETE FROM medicos WHERE id_medicos = %s"
    val = (id_medicos,)
    cursor.execute(sql, val)
    mydb.commit()

    sql = "DELETE FROM endereco WHERE id_endereco = %s"  # Deletando endereco
    val = (id_endereco[6],)
    cursor.execute(sql, val)
    mydb.commit()

    return cursor.rowcount


#Funcionando e testado
#create_medicos("546546546","afdasfdadas","fniwnguwn","564654645465","sjgfhdjghsfdjgh","sfjhosjhkdffjkh","132132-56","46556","asdhkabhds")
#print(read_medicos("1"))
#update_medicos("1","7463276","atualizando o medico","att","234432","sfdgfgdsfgds","att","13132213","432567","asdasdasd")
#delete_medicos("1")