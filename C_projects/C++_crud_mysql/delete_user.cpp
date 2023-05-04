#include <iostream>
#include <cstdlib>
#include <string>
#include <sstream>

#include <mysql_connection.h>
#include <mysql_driver.h>
#include <cppconn/driver.h>
#include <cppconn/exception.h>
#include <cppconn/resultset.h>
#include <cppconn/statement.h>

using namespace std;

void create_user(sql::Connection* con, string name, int age) {
    try {
        // prepare a SQL statement to insert the new user into the database
        sql::Statement* stmt = con->createStatement();
        stringstream ss;
        ss << "INSERT INTO users (name, age) VALUES ('" << name << "', " << age << ")";
        stmt->execute(ss.str());
        cout << "User created successfully" << endl;
        delete stmt;
    } catch (sql::SQLException& e) {
        cout << "SQL Exception: " << e.what() << endl;
    }
}

void delete_user(sql::Connection* con, string name) {
    try {
        sql::Statement* stmt = con->createStatement();
        stringstream ss;
        ss << "DELETE FROM users WHERE name = '" << name << "'";
        stmt->execute(ss.str());
        cout << "User delete successfully" << endl;
        delete stmt;
    } catch (sql::SQLException& e) {
        cout << "SQL Exception: " << e.what() << endl;
    }
}

void update_user(sql::Connection* con, string name, string new_name, int new_age) {
    try {
        // prepare a SQL statement to insert the new user into the database
        sql::Statement* stmt = con->createStatement();
        stringstream ss;
        
        if(name == "") {
            cout << "Insira um nome para realizar a atualização: ";
            exit(0);
        }

        if(new_name == "" && (new_age != 0 || new_age != NULL))
            ss << "UPDATE users SET age = '" << new_age << "' WHERE name = '" << name << "'";
        else if((new_age == 0 || new_age == NULL) && (new_name != ""))
            ss << "UPDATE users SET name = '" << new_name << "' WHERE name = '" << name << "'";
        else if(new_name == "" && (new_age == 0 || new_age == NULL)) {
            cout << "Nothing to update" << endl;
            exit(0);
        }
        else if(new_name != "" && (new_age != 0 || new_age != NULL))
        ss << "UPDATE users SET name = '" << new_name << "', age = '" << new_age << "' WHERE name = '" << name << "'";
        stmt->execute(ss.str());
        cout << "User update successfully" << endl;
        delete stmt;
    } catch (sql::SQLException& e) {
        cout << "SQL Exception: " << e.what() << endl;
    }
}

void read_users(sql::Connection* con) {
    try {
        // prepare a SQL statement to select all users from the database
        sql::Statement* stmt = con->createStatement();
        sql::ResultSet* res = stmt->executeQuery("SELECT * FROM users");

        // iterate through the result set and display the user information on the console
        while (res->next()) {
            cout << "Name: " << res->getString("name") << endl;
            cout << "Age: " << res->getInt("age") << endl;
        }
        delete res;
        delete stmt;
    } catch (sql::SQLException& e) {
        cout << "SQL Exception: " << e.what() << endl;
    }
}

int main() {
    try {
        sql::Driver* driver;
        sql::Connection* con;
        int new_age;
        string name;
        string new_name;

        // create a MySQL driver instance
        driver = get_driver_instance();

        // create a MySQL connection instance
        con = driver->connect("tcp://localhost:3306", "root", "password");

        // specify the MySQL schema to use
        con->setSchema("mydbtest");

        cout << "Enter name: ";
        cin >> name;
        cout << "Enter new name: ";
        cin >> new_name;
        cout << "Enter new age: ";
        cin >> new_age;

        // call the create_user function to save the user information to the database
        //create_user(con, name, age);
        update_user(con, name, new_name, new_age);
        // clean up
        delete con;
    } catch (sql::SQLException& e) {
        cout << "SQL Exception: " << e.what() << endl;
    }

    return 0;
}
