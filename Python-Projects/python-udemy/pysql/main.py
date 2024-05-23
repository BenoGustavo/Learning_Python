# PyMySQL - um cliente MySQL feito em Python Puro
# Doc: https://pymysql.readthedocs.io/en/latest/
# Pypy: https://pypi.org/project/pymysql/
# GitHub: https://github.com/PyMySQL/PyMySQL
import os
from typing import cast, Tuple

import dotenv
import pymysql
import pymysql.cursors
import pymysql.err

class DatabaseController:
    def __init__(self,CURRENT_CURSOR):
        self.__connection = False
        self.__currentCursor = CURRENT_CURSOR

    def makeConnection(self):
        try:
            connection = pymysql.connect(
            host=os.environ['MYSQL_HOST'],
            user=os.environ['MYSQL_USER'],
            password=os.environ['MYSQL_PASSWORD'],
            database=os.environ['MYSQL_DATABASE'],
            charset='utf8mb4',
            cursorclass=self.__currentCursor,
        )
            
            self.__connection = connection
        except pymysql.err.OperationalError as e:
            print("Error: ", e, "- perhaps the database is not running? or you don't filled the .env file correctly?")

    def createTable(self,tableName):
        self.makeConnection()
        with self.__connection:
            with self.__connection.cursor() as cursor:
                cursor.execute(  # type: ignore
                    f'CREATE TABLE IF NOT EXISTS {tableName} ('
                    'id INT NOT NULL AUTO_INCREMENT, '
                    'nome VARCHAR(50) NOT NULL, '
                    'idade INT NOT NULL, '
                    'PRIMARY KEY (id)'
                    ') '
                )
            self.__connection.commit()

    def cleanTable(self,tableName):
        self.makeConnection()
        with self.__connection:
            with self.__connection.cursor() as cursor:
                cursor.execute(f'TRUNCATE TABLE {tableName}')

    def insertData(self, tableName, data: Tuple[str, int]):
        self.makeConnection()
        with self.__connection.cursor() as cursor:
            sql = (
                f'INSERT INTO {tableName} '
                '(nome, idade) '
                'VALUES '
                '(%s, %s) '
            )
            cursor.execute(sql, data)
        
        self.__connection.commit()

    def insertDataWithDict(self, tableName, data: dict[str: str or int]):
        self.makeConnection()
        with self.__connection.cursor() as cursor:
            sql = (
                f'INSERT INTO {tableName} '
                '(nome, idade) '
                'VALUES '
                '(%(name)s, %(age)s) '
            )
            cursor.execute(sql, data)
        
        self.__connection.commit()

    def insertManyData(self, tableName, data: Tuple[Tuple[str, int]]):
        self.makeConnection()
        with self.__connection.cursor() as cursor:
            sql = (
                f'INSERT INTO {tableName} '
                '(nome, idade) '
                'VALUES '
                '(%s, %s) '
            )
            
            #this iterates over the tuple of tuples and insert each tuple
            cursor.executemany(sql, data)
        
        self.__connection.commit()

    def insertManyDataWithDict(self, tableName, data: Tuple[dict[str: str or int]]):
        self.makeConnection()
        with self.__connection.cursor() as cursor:
            sql = (
                f'INSERT INTO {tableName} '
                '(nome, idade) '
                'VALUES '
                '(%(name)s, %(age)s) '
            )
            
            #this iterates over the tuple of dicts and insert each dict
            cursor.executemany(sql, data)
        
        self.__connection.commit()

    def selectBetween(self, tableName, lowerId, upperId):
        self.makeConnection()
        with self.__connection.cursor() as cursor:
            sql = (
                f'SELECT * FROM {tableName} '
                'WHERE id BETWEEN %s AND %s  '
            )

            cursor.execute(sql, (lowerId, upperId))
            
            data = cursor.fetchall()
            return data
        
    def selectAll(self, tableName):
        self.makeConnection()
        with self.__connection.cursor() as cursor:
            cursor.execute(f'SELECT * FROM {tableName} ')
            data = cursor.fetchall()
            return data
        
    def deleteData(self, tableName, id):
        self.makeConnection()
        with self.__connection.cursor() as cursor:
            sql = (
                f'DELETE FROM {tableName} '
                'WHERE id = %s'
            )
            cursor.execute(sql, (id,))

        self.__connection.commit()

    def updateData(self, tableName, data: Tuple[str, int, int]):
        self.makeConnection()
        with self.__connection.cursor() as cursor:
            sql = (
                f'UPDATE {tableName} '
                'SET nome=%s, idade=%s '
                'WHERE id=%s'
            )
            cursor.execute(sql, data)

        self.__connection.commit()

    def usefullInfo(self):
        self.makeConnection()
        with self.__connection.cursor() as cursor:
            cursor.execute(
                f'SELECT id from {TABLE_NAME} ORDER BY id DESC LIMIT 1'
            )
            lastIdFromSelect = cursor.fetchone()

            resultFromSelect = cursor.execute(f'SELECT * FROM {TABLE_NAME} ')

            data6 = cursor.fetchall()

            for row in data6:
                print(row)

            print('resultFromSelect', resultFromSelect)
            # contains the number of rows affected by the last executed operation
            print('len(data6)', len(data6))
            # contains the number of rows affected by the last executed operation
            print('rowcount:', cursor.rowcount)
            # contains the ID generated for an AUTO_INCREMENT column by the previous INSERT or UPDATE statement
            print('lastrowid', cursor.lastrowid)
            # contains the ID generated for an AUTO_INCREMENT column by the previous INSERT or UPDATE statement
            print('lastrowid by hand', lastIdFromSelect)

            cursor.scroll(0, 'absolute')
            # contains the current 0-based index of the cursor in the result set or None if the cursor is not positioned on a row
            print('rownumber', cursor.rownumber)
        self.__connection.commit()

if __name__ == "__main__":
    TABLE_NAME = 'customers'
    CURRENT_CURSOR = pymysql.cursors.DictCursor

    dotenv.load_dotenv()

    db = DatabaseController(CURRENT_CURSOR)
    db.createTable(TABLE_NAME)
    db.cleanTable(TABLE_NAME)
    db.insertData(TABLE_NAME, ('John', 25))
    db.insertDataWithDict(TABLE_NAME, {'name': 'Paul', 'age': 33})
    db.insertManyData(TABLE_NAME, (('George', 22), ('Ringo', 21)))
    db.insertManyDataWithDict(TABLE_NAME, ({'name': 'Yoko', 'age': 30}, {'name': 'Lennon', 'age': 40}))
    print(db.selectBetween(TABLE_NAME, 1, 3))
    print(db.selectAll(TABLE_NAME))
    db.deleteData(TABLE_NAME, 1)
    db.updateData(TABLE_NAME, ('JohnMudado', 26, 2))
    db.usefullInfo()