import os
import extractor as ext
import BBDD as bd
#Para comenzar vamos a instalar en el sistema las aplicaciones que se necesitan para hsceer funcionar el programa

#Al iniciar el programa cargamos un fichero con la factura 

""" EN ESTE CASO EL FICHERO VIENE DADO POR UNA RUTA COMO PRUEBA """
path = os.getcwd()+'\\files\\fichero4.pdf'

#Vamos a extraer de ese fichero los datos de la compra y realizamos su insercion en la base de datos

""" LO PRIMERO ES EXTAER EL TEXTO DEL ARCHIVO PDF """
text = ext.extractTextPDF(path)

"""CONVERTIMOS EL TEXTO EXTRAIDO EN UNA LISTA DE LINEAS PARA PODER TRABAJAR CON ELLAS"""
lines = text.split('\n')

#Ahora realizamos la insercion en la base de datos de la compra y de los articulos de dicha compra

"""CREAMOS UNA COMPRA LLAMANDO AL METODO extractDataPurchase()"""
purchase = list(ext.extractDataPurchase(lines))

""" AHORA LLAMAMOS AL METODO PARA EXTRAER LOS ARTICULOS PASANDOLE COMO PARAMETRO LA LISTA CREADA ANTERIORMENTE lines
Y GENERAMOS UNA LISTA DE ARTICULOS CON EL METODO extractArticles() PASANDOLE COMO PARAMETRO TAMBIEN EL CODIGO DE COMPRA"""
articles = ext.extractArticles(lines,purchase[2])
"""GUARDAMOS EL TOTAL DE LA COMPRA EL LA VARIABLE PURCHASE"""
purchase.append(ext.extractPrice(articles))
"""REALIZAMOS LA INSEERCCION A LA BASE DE DATOS DE LA COMPRA Y DE LOS ARTICULOS"""
bd.insertar(purchase)
bd.insertar(articles)


#Sacar el menu para que el ususario eliga la opcion que quiera consultar