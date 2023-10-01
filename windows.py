import tkinter as tk
import tkinter.messagebox as mbox
from tkinter import filedialog
import pathlib as pb

# creamos una varibale global para acceder desde los distinotso archivoa para guardar la ruta del fichero seleccionado

path = ''

#Creamos una instance de tkinter mediante el metodo createWindows()

def createWindow(title,size):
    #Cremaos un objeto de la clase tkinter
    window = tk.Tk()
    
    #Le asiganmos un tamanio y le ponemos la opcion de que no sea de tamaño dinamico
    window.geometry(size)
    window.resizable(0,0)
    
    #Le aignamos un titulo y una etoqueta que se muestre cuando se abra
    window.title(title)
    label = tk.Label(window,text='Carga de Fichero')
    
    return window
  
#Funcion para crear un boton de carga de archivos
def createLoadButton(window,path):
# Crear un botón para cargar el archivo, con el texto de cargar archivo y cuando se pulsa va a llamar a la funcooin fileLoader()
    return tk.Button(window, text="Load File", command = lambda :fileLoader(path))

#Funcion para cargar un archivo desde tu pc

def fileLoader(path):
    #Crea un fichero dentro de los parametros establecidos dentro de ls funcion filedialog.askopenfilename(),
    #si el archivo existe lo retorna si no manda un error por la consola
    file = filedialog.askopenfilename(filetypes=[("Archivos de texto", "*.pdf"), ("Todos los archivos", "*.*")])
    # Si se ha proporcionado una archivo o direccion valida
    if file :
        path = file
