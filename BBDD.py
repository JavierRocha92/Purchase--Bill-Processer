#Vamos a crear una conexion con la base de datos para insertar las compras con sus distintos productos
#Importamos sqlite3
import sqlite3
import processor as proc
#Creamos un metodo para conectarnos a la base de datos
def conectar ():
    conexion = sqlite3.connect('Purchase.db')
    cursor = conexion.cursor()
    return conexion, cursor

#Creamos una funcion para consultar los datos de una tabla
def consulta (statement):
    conexion, cursor = conectar()
    
    if (cursor.execute(statement)):
        return cursor.fetchall()
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
            INSERT INTO purchase(date,code,price) VALUES(?,?,?)'''
        
        if (cursor.execute(statement,p)):
            print('la inserccion de ha realizado correctamente')
        else:
            print('Ha ocurrido algun error')
            
    cursor.close()
    conexion.commit()
    conexion.close()
    
    
    
#Creamos una funcion para encontrar el articulo mas caro de las compras segun el precio de la unidad

def findExpensive():
    
    # Llamaos a metodo para sacar el nombre y el precio medio del articulo que sea mas caro por su ud_price
    
    article = consulta('''
    SELECT name,AVG(price) precio_medio FROM ARTICLES WHERE name = (SELECT name FROM ARTICLES WHERE PRICE = 
    (SELECT MAX(price) FROM ARTICLES))''')
    
    # mostramos por pantalla el articulo en el que mas dinero se ha gastado
    
    print(f'El articulo mas caro  es : {article[0][0]} con un precio media por unidad de  : {article[0][1]} €')
    
    
    
    
#Creamos una funcion para encontrar el articulo que mas dinero ha sido gastado en todas las compras

def findExpensiveAmount():
    
    # Llamamos a metodo de consulta para buscar el articulo mque mas dinero se ha gastado
    article = consulta('''
    SELECT name,ROUND(SUM(price),2) FROM ARTICLES GROUP BY name HAVING SUM(price) = 
    (SELECT MAX(total) FROM (SELECT SUM(price) AS total FROM ARTICLES GROUP BY name))''')
    
    # mostramos por pantalla el articulo en el que mas dinero se ha gastado
    
    print(f'El articulo en el que mas dinero te has gastado es : {article[0][0]} con un balance de : {article[0][1]} €')
    
    
    
#Creamos una funcion para encontrar el articulo que mas ha sido comprado

def findMostOrdered():
    # Llamamos a metodo de consulta para buscar el articulo que mas ha sido comprado
    article = consulta('''
    SELECT name,SUM(uds) FROM ARTICLES GROUP BY name HAVING SUM(uds) = 
    (SELECT MAX(total) FROM (SELECT SUM(uds) AS total FROM ARTICLES GROUP BY name))''')
    
    # mostramos por pantalla el articulo mas comprado
    
    print(f'El articulo mas comprado es : {article[0][0]} con un total de {article[0][1]} uidades')
    
    
# Metodo para calcular el precio historico de todas las compras

def totalPrice():
    price = consulta('''
    SELECT ROUND(SUM(price),2) FROM PURCHASE ''')
    
    # mostramos por pantalla la consulta que hemos recibido
    
    print(f'El precio total es : {price[0][0]}')
    

# Metodo para sacar el precio total de un mes y el precio media respecto al año     
    
def priceFilterMonth(month):
    
# declaramos una lista con los nombres de los mese para mostrar la salida por pantalla

    months = ['Enero','Febrero','Marzo','Abril','mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']
    
# pasamos en valor de month a tipo string para poder trabajar con el

    month = str(month)
    
    # vamos a porcesar la varibale month para saber si tiene o no dos unidades para añadirle un cero el principio si solo tuviera una
    
    if len(month) == 1:
        month = '0' + month
    
    # guardamos lo que nos devuelven las consultas rn variables para poder operar con ellas
    
    monthAmount = consulta(f'''
             SELECT round(sum(price),2)  FROM purchase WHERE strftime('%m', date) = "{month}"''')
    yearAmount = consulta('''
             SELECT SUM(price),COUNT(*) FROM purchase''')
    # realizmos la consulta con la fucnion que se puede ver a continuacion ya que es la indicada para procesar dates que estan guardadads como varchar en formato ISO
    print(f'El precio gastado en el mes : {months[int(month) - 1]} es de :',
    monthAmount[0][0],
    '€ el precio gastado en el año hasta ahora es de :',
    yearAmount[0][0],
    '€ el precio medio de gasto por compra en lo que va de año es de : ',round(float(yearAmount[0][0]) / float(yearAmount[0][1]),2),' €'
    )
    
    # metodo para mostrar los prodcutos de una compra especifica en funcion de una fecha prporcionada
    
def showPurchase():
    words = ['dia','mes','ano']
    date = []
    
    #pedimos los valores de la fecha la ususario para poder extraer los articulos de una compra
    
    for word in words:
        date.append(input(f'Inserta un valor para {word}'))
    
    # llamamos a metodo para porcesar la fecha del usuario para poder realizar la consulta
    
    date = proc.processDateSelect(date)
    
    # guardamos lo que nos devuleve la consulta en un varibale
        
    articles = consulta(f'''
                        SELECT * FROM articles WHERE code IN (SELECT code FROM purchase WHERE 
                        strftime('%d', date) = "{date[0]}" AND strftime('%m', date) = "{date[1]}" AND strftime('%Y', date) = "{date[2]}")''')
    
    # realizamos un bucle for para mostrar por pantalla todos los articulos de esa compra
    
    for article in articles :
        print(article)
            