#Vamos a crear una conexion con la base de datos para insertar las compras con sus distintos productos
#Importamos sqlite3
import sqlite3

#Creamos un metodo para conectarnos a la base de datos
def conectar ():
    conexion = sqlite3.connect('Purchase.db')
    cursor = conexion.cursor()
    return conexion, cursor

#Creamos una funcion para consultar los datos de una tabla
def consulta (p):
    conexion, cursor = conectar()
    statement =  '''
        SELECT * FROM purchase(codigo, nombre, peso, precio_ud, precio ) VALUES(?,?,?,?,?)'''
    if (cursor.execute(statement)):
        print('la inserccion de ha realizado correctamente')
    else:
        print('Ha ocurrido algun error')
    cursor.close()
    conexion.commit()
    conexion.close()
    
#Creamos una funcion para consultar los datos de una tabla
def insertar (p):
    conexion, cursor = conectar()
    statement =  '''
        INSERT INTO purchase(codigo, nombre, peso, precio_ud, precio ) VALUES(?,?,?,?,?)'''
    if (cursor.execute(statement,p)):
        print('la inserccion de ha realizado correctamente')
    else:
        print('Ha ocurrido algun error')
    cursor.close()
    conexion.commit()
    conexion.close()
    
    
    
#Creamos una funcion para encontrar el articulo mas caro de las compras segun el precio de la unidad

def findExpensive():
    conexion, cursor = conectar()
    statement = '''
    SELECT nombre, precio FROM PURCHASE WHERE precio_ud = (SELECT MAX(precio_ud) FROM PURCHASE)'''
    
    if (cursor.execute(statement)):
        result = cursor.fetchall()
        for data in result:
            print(data[0],' ----> ',data[1],' €')
    else:
        print('Ha ocurrido algun error')
    cursor.close()
    conexion.commit()
    conexion.close()
    
#Creamos una funcion para encontrar el articulo mas caro de las compras segun el precio de la unidad

def findMostExpensive():
    conexion, cursor = conectar()
    statement = '''
    SELECT nombre, precio FROM PURCHASE WHERE precio = (SELECT MAX(precio) FROM PURCHASE)'''
    
    if (cursor.execute(statement)):
        result = cursor.fetchall()
        for data in result:
            print(data[0],' ----> ',data[1],' €')
    else:
        print('Ha ocurrido algun error')
    cursor.close()
    conexion.commit()
    conexion.close()
    