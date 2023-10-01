#Vamos a crear una conexion con la base de datos para insertar las compras con sus distintos productos
#Importamos sqlite3
import sqlite3
import BBDD as bd
import tkinter as tk
import tkinter.messagebox as mbox
from tkinter import filedialog
import pathlib as pb
import windows as wn
import menu
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
                date VARCHAR(16) NOT NULL,
                price FLOAT(2,2) NOT NULL
                   )'''
    
    
# createTable(statementArt)
# createTable(statementPur) 


option = 1

while(option != 0):
    menu.menu()
    option = int(input())
    match(option):
        case 1:
            menu.menuArticles()
            option = int(input())
            match(option):
                case 1:#el articulo mas caro por precio unidad
                    bd.findExpensive()           
                    break
                case 2:#el articulo mas comprado
                    bd.findMostOrdered()
                    break
                case 3:#el articulo en el que mas dinero se ha gastado
                    bd.findExpensiveAmount()
                    break
        case 2:
            menu.menuPurchase()
            option = int(input())
            match(option):
                case 1:#el precio total historico de todas las compras
                    bd.totalPrice()
                    break
                case 2:#precio de gasto de mes dado del año entero y del precio medio qeu supone al año
                    month = int(input('indica el numero de mes'))
                    bd.priceFilterMonth(month)
                    break
                case 3:#todos los elementos de una compra especifica segun su fecha
                    bd.showPurchase()
                    break
            break
'''FALTA PASAR LAS FECHAS DE LAS COMPRAS A FORMATO DATE PARA PODER ORCESARLAS EN LAS CONSULTAS'''
