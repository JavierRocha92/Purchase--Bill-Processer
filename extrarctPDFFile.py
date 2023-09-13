import re
import os
from Product import Product
from Purchase import Purchase
import processor as proc
import extractor as ext
    
#Genramos un aruta para tener nuestro fichero
path = os.getcwd()+'\\files\\fichero2.pdf'

#Lalammaos a metodo para leer el fichero pdf que le mandamos como parametro(ruta)
# y nos devulve el texto de dicho fichero
text = ext.extractTextPDF(path)

#Ahora mediante split separamos las distitas lineas del fichero
lines = text.split('\n')

#Esta expresion regular nos incidica el final d la busqueda, ya que no empieza por un numero,
#la fila que queremos dejar de leer
start = re.compile(r'\d')

#esta re la vamos a usar para el split cuando creamos la vaiable producto para separar en strings
# los valores y crear una lista
precio = re.compile(r'^\d+,\d\d')

#Creamos las variable que nos hacen falta para procesar el texto del fichero PDF
fruit = ''
collect = False
#Creamos un objeto de la clase Purchase y le agregamos la ficha del fichero
purchase = Purchase(date = ext.extractDate(path))

#Ahora vamos a leer solo la informacion de los productos, el inicio es la linea en la posicion 7
#Creamos un bucle for desde la posicion 7 del texto hasta el final para encontrar la ultima linea,
#usando la expresion regular y saliend del bucle con ella
for line in lines[7:]:
    #Creamos un producto y le separamos por el split de espacios en blanco
    pr = line.split()
    #realizamos un if para con la regex creada anteiormente (start) podamos salir del bucle 
    if start.match(pr[0]):
        #Usamos un condicional para saber si el producto que estamos leyendo tiene uno o mas parametros
        #para saber si estamos procesando un producto con peso o no
        if  len(pr) > 1: 
            #Llamamos al metodo para obtener la inea de datos procesada segun sus campos
            product = proc.processLine(precio,pr)
            #Evaluamos si la condicion de fruta esta en True para poder unir la informacion de la fruta
            # con la inea actual que se esta procesando
            if collect == True:
                fruit.extend(product)
                product = proc.processText(fruit) 
                #Creamos un objeto producto y lo agregamos a la compra
                p = Product(product[0],product[1],product[2],product[3],product[5])
                purchase.products.append(p)
            #Ponemos la variable collect a False
                collect=False
            else:
                product = proc.processText(pr)
                #Este condicional nos va a decir si el producto tiene un o mas unidades de compra
                if product[0] == '1':
                #Creamos un objeto de la clase Product
                    p = Product(ud = product[0], name = product[1], price = product[2])
                else:
                    p = Product(ud = product[0], name = product[1], ud_price = product[2], price = product[3])
                #Llamamos a metodo para procesar los precio
                purchase.products.append(p)            
                
        else:
            #Si la longitud del producto es de 1 esto indca que es una fruta, debemos de dejar gaurdada
            # la informaicon de esta para unirla con sus datos ya que aparaeceran en la siguiente linea
            collect = True
            fruit = pr
    else:
        break

#Cragamos el valor total de la compra llamansdo al metodo
purchase.total_price = purchase.setTotalPrice()
print(len(purchase.products))
for product in purchase.products:
    print(product)
print(purchase)


