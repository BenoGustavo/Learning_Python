import mysql.connector

# Conectando ao schema

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="hospital_v2"
)

# CRUD paciente

# Criando paciente


def create_paciente(CPF, nome, email, telefone, logradouro, doenca, cep, numero, bairro):

    # Criando endereco para o paciente
    def create_endereco(logradouro, cep, numero, bairro):

        cursor = mydb.cursor()
        # Comando mysql
        sql = "INSERT INTO endereco (logradouro, cep, numero, bairro) VALUES (%s, %s, %s, %s)"
        val = (logradouro, cep, numero, bairro)
        cursor.execute(sql, val)
        mydb.commit()
        return cursor.lastrowid

    # Chamando a funcao que cria o endereco para o paciente
    create_endereco(logradouro, cep, numero, bairro)

    cursor = mydb.cursor()

    # Selecionando o ID do endereco
    sql = "SELECT * FROM endereco ORDER BY id_endereco DESC LIMIT 1"
    cursor.execute(sql)
    id_endereco = cursor.fetchone()

    # Tenta criar o paciente, se não conseguir deleta seu endereco e então finaliza a funcao

    try:
        # Criando o paciente, junto com o ID do respectivo endereco
        sql = "INSERT INTO paciente (CPF, nome, email, telefone ,doenca, id_endereco) VALUES (%s, %s, %s,%s,%s,%s)"
        val = (CPF, nome, email, telefone, doenca, id_endereco[0],)
        cursor.execute(sql, val)
        mydb.commit()
    except:
        # Selecionando informaçoes
        sql = "SELECT * FROM endereco ORDER BY id_endereco DESC LIMIT 1"
        cursor.execute(sql)
        result = cursor.fetchone()

        sql = "DELETE FROM endereco WHERE id_endereco = %s"
        # o primeiro elemento de 'result' é o ID da última linha
        val = (result[0],)
        cursor.execute(sql, val)
        mydb.commit()

    finally:
        return cursor.lastrowid


# Lendo informacoes da tabela paciente
def read_paciente(id_paciente):
    cursor = mydb.cursor()
    # Comando mysql || pegando informacoes do paciente com ID
    sql = "SELECT * FROM paciente WHERE id_paciente = %s"
    val = (id_paciente,)
    cursor.execute(sql, val)
    result = cursor.fetchone()

    # Comando mysql || pegando informacoes do endereco paciente
    sql = "SELECT * FROM endereco WHERE id_endereco = %s"
    val = (result[6],)
    cursor.execute(sql, val)
    endereco = cursor.fetchone()

    # Retornando informacoes
    if result is None or endereco is None:
        return None
    return {'id': result[0], 'CPF': result[1], 'nome': result[2], 'email': result[3], "telefone": result[4], "doenca": result[5], 'logradouro': endereco[1], 'cep': endereco[2], 'numero': endereco[3], 'bairro': endereco[4]}

# Atuailizando informacoes paciente


def update_paciente(id_paciente, CPF, nome, email, telefone, logradouro, doenca, cep, numero, bairro):
    cursor = mydb.cursor()
    # Comando mysql || atulizando dados
    sql = "UPDATE paciente SET CPF = %s, nome = %s, email = %s, telefone = %s, doenca = %s WHERE id_paciente = %s"
    val = (CPF, nome, email, telefone, doenca, id_paciente)
    cursor.execute(sql, val)
    mydb.commit()

    sql = "SELECT * FROM paciente WHERE id_endereco = %s"  # Selecionando ID endereco
    id = (id_paciente,)
    cursor.execute(sql, id)
    endereco = cursor.fetchone()  # Armazenando ID endereco

    # Atuailizando informacoes endereco
    def update_endereco(logradouro, cep, numero, bairro, endereco):

        # Comando mysql || Atuailizar informacoes endereco do paciente
        sql = "UPDATE endereco SET logradouro = %s, cep = %s, numero = %s, bairro = %s WHERE id_endereco = %s"
        val = (logradouro, cep, numero, bairro, endereco)
        cursor.execute(sql, val)
        mydb.commit()
        return cursor.rowcount

    # doenca que atualiza o endereco
    update_endereco(logradouro, cep, numero, bairro, endereco[6])

    return cursor.rowcount

# Deletando dados paciente


def delete_paciente(id_paciente):

    cursor = mydb.cursor()
    sql = "SELECT * FROM paciente WHERE id_paciente = %s"  # Selecionando ID endereco
    id = (id_paciente,)
    cursor.execute(sql, id)
    id_endereco = cursor.fetchone()  # Armazenando ID endereco

    # Deletando endereco || RECEBENDO ERRO POIS N POSSO DELETAR CHAVE ESTRANGEIRA
    sql = "DELETE FROM endereco WHERE id_endereco = %s"
    val = (id_endereco[6],)
    cursor.execute(sql, val)

    cursor = mydb.cursor()
    # Deletando informacoes do paciente
    sql = "DELETE FROM paciente WHERE id_paciente = %s"
    val = (id_paciente,)
    cursor.execute(sql, val)
    mydb.commit()

    return cursor.rowcount

# Funcionando

# update_paciente("1","55555","teste update","testeupdate@gmail.com","987789","teste update","teste update","56798761","456654","teste update")
# create_paciente("123","nome","nome@gmail.com","3245","logra a douro","rinite","666666","987","barro")
# print(read_paciente("1"))
