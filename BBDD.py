#Vamos a crear una conexion con la base de datos para insertar las compras con sus distintos productos
#Importamos sqlite3
import sqlite3

#Creamos un metodo para conectarnos a la base de datos
def conectar ():
    conexion = sqlite3.connect('Purchase.db')
    cursor = conexion.cursor()
    return conexion, cursor

#Creamos una funcion para consultar los datos de una tabla
def consulta (statement):
    conexion, cursor = conectar()
    
    if (cursor.execute(statement)):
        for e in cursor.fetchall():
            print(e)
    else:
        print('Ha ocurrido algun error')
    cursor.close()
    conexion.commit()
    conexion.close()

    
#Creamos una funcion para consultar los datos de una tabla
def insertar (p):
    conexion, cursor = conectar()
    #Comprobamos si el primer elemento de lal lista qye nos pasan por parametro es una lista para insertar los articulos
    # y si no sera un string y en dicho caso insertaremos una compra
    if(isinstance(p[0],list)):
    #Para insertar un articulo
        statement =  '''
            INSERT INTO articles(code, uds, name, weight, ud_price, price) VALUES(?,?,?,?,?,?)'''
        if (cursor.executemany(statement,p)):
            print('la inserccion de ha realizado correctamente')
        else:
            print('Ha ocurrido algun error')
    else:
        #para insertar una compra
        statement =  '''
            INSERT INTO purchase(date,hour,code,price) VALUES(?,?,?,?)'''
        
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
    