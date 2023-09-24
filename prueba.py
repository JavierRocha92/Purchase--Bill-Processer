#Vamos a crear una conexion con la base de datos para insertar las compras con sus distintos productos
#Importamos sqlite3
import sqlite3
import BBDD as bd


def createTable(statement):
    conexion , cursor = bd.conectar()
    
    if (cursor.execute(statement)):
        print('la creacion de la tabla se ha realizado correctamente')
    else:
        print('Ha ocurrido algun error')
    cursor.close()
    conexion.commit()
    conexion.close()
    
    
statementArt = '''CREATE TABLE IF NOT EXISTS articles (
                code NOT NULL,
                uds INTEGER NOT NULL,
                name VARCHAR(20) NOT NULL,
                weight FLOAT(2,2) NOT NULL,
                ud_price FLOAT(2,2) NOT NULL,
                price FLOAT(2,2) NOT NULL,
                PRIMARY KEY (code, name),
                FOREIGN KEY (code) REFERENCES purchase(code)
                    )'''
                    
statementPur =  '''CREATE TABLE IF NOT EXISTS purchase (
                code INTEGER PRIMARY KEY NOT NULL,
                date VARCHAR(10) NOT NULL,
                hour VARCHAR(10) NOT NULL,
                price FLOAT(2,2)
                   )'''
    
    
""" createTable(statementArt)
createTable(statementPur) """
""" bd.findExpensive()
bd.findMostExpensive() """

statement = """SELECT date,p.code,count(*) numeroArticulos FROM articles a join purchase p on a.code = p.code GROUP BY p.code """
bd.consulta(statement)