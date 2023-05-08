#include <iostream>
#include <cstdlib>
#include <string>
#include <sstream>

/*
#include "c:\Program Files\MySQL\Connector C++ 8.0\include\jdbc\mysql_connection.h"
#include "c:\Program Files\MySQL\Connector C++ 8.0\include\jdbc\mysql_driver.h"
#include "c:\Program Files\MySQL\Connector C++ 8.0\include\jdbc\cppconn\driver.h"
#include "c:\Program Files\MySQL\Connector C++ 8.0\include\jdbc\cppconn\exception.h"
#include "c:\Program Files\MySQL\Connector C++ 8.0\include\jdbc\cppconn\resultset.h"
#include "c:\Program Files\MySQL\Connector C++ 8.0\include\jdbc\cppconn\statement.h"
*/

/*
#include "C_projects/C++_crud_mysql/Connector C++ 8.0/include/jdbc/mysql_connection.h"
#include "C_projects/C++_crud_mysql/Connector C++ 8.0/include/jdbc/mysql_driver.h"
#include "C_projects/C++_crud_mysql/Connector C++ 8.0/include/jdbc/cppconn/driver.h"
#include "C_projects/C++_crud_mysql/Connector C++ 8.0/include/jdbc/cppconn/exception.h"
#include "C_projects/C++_crud_mysql/Connector C++ 8.0/include/jdbc/cppconn/resultset.h"
#include "C_projects/C++_crud_mysql/Connector C++ 8.0/include/jdbc/cppconn/statement.h"
*/


#include <mysql_connection.h>
#include <mysql_driver.h>
#include <cppconn/driver.h>
#include <cppconn/exception.h>
#include <cppconn/resultset.h>
#include <cppconn/statement.h>

using namespace std;

//Criando funcionario
void create_funcionario(sql::Connection* con, string cpf, string nome, string email, string telefone, string funcao, string logradouro, string cep, string numero, string bairro) {  

    //Criando endereço para o funcionario
    try{

        sql::Statement* stmt = con->createStatement();
        stringstream ss;

            //Inserindo as informações na tabela endereço

        ss << "INSERT INTO endereco (logradouro, cep, numero, bairro) VALUES (" << logradouro << ", " << cep << ", " << numero << "," << bairro <<")";

            //Executando comando mysql

        stmt->execute(ss.str());
        cout << "Endereco criado com sucesso" << endl; //Status
        delete stmt;
    } catch(sql::SQLException& sqlerror){
        //cout << "SQL Exception: " << sqlerror.what() << endl; //Status
    }
    
    try{

        sql::Statement* stmt = con->createStatement();

        //Selecionando ID do endereco criado
        sql::ResultSet* res = stmt->executeQuery("SELECT * FROM endereco ORDER BY id_endereco DESC LIMIT 1");

        delete stmt;

        stringstream ss;

        //Inserindo as informações na tabela funcionario
        ss << "INSERT INTO funcionario (CPF, nome, email, telefone ,funcao, id_endereco) VALUES ('" << cpf << ", " << nome << ", " << email << "," << telefone << "," << funcao << "," << res <<")";

        //Executando comando mysql
        stmt->execute(ss.str());
        cout << "Funcionario criado com sucesso" << endl; //Status
        delete stmt;
    
    } catch(sql::SQLException& sqlerror){
        //cout << "SQL Exception: " << sqlerror.what() << endl; //Status
        }
}
