import tkinter as tk
import tkinter.messagebox as mbox
from tkinter import filedialog
#Creamos una instance de tkinter mediante el metodo createWindows()

def createWindows():
    """FUNCION QUE RETORNA UNA INSTANCIA DE TKINTER"""
    return tk.Tk()
#Le damos un atamaño a una ventana ya creada recibiendo como parametro las medidas de ls ventana con sizeWindows()

def sizeWindows(window,size):
    """FUNCION QUE RETORNA UN OBJETO TKINTER CON EL TAMANIO CAMBIADO"""
    return window.geometry('600x600')

#Metodo para generar una ventana con los elementos necesarios para que el usuario pueda elegir un fichero de su pc

def chooseFile():
    #Llamamos a metodo para creae un objeto de la clase tk
    wmain = createWindows();
    #Ahora lw asignamos un tamaño
    

wroot = createWindows()

wroot.title('main')

wroot.geometry('600x600')

#para no cambiar el tamaño de la ventana
 
wroot.resizable(0,0)

#paraponer una etiqueta

cabecera = tk.Label(wroot, text='Ventana Principal').pack()

#Para crear un boton con texto

boton = tk.Button(wroot,text='haz click')
boton.pack()
#Para crea un marco

marco = tk.Frame(wroot)
marco.pack()

#Para crea un evento sobre que se ha pulsado un boton
def showClick(event):
    print('has pulsado el boton')
boton.bind('<Button-1>',showClick)

#Para abrir una ventana secundaria

def abrir_ventana_modal():
    ventana_modal = tk.Toplevel(wroot)
    ventana_modal.title("Ventana Modal")
    # Agregar widgets a la ventana_modal

boton_modal = tk.Button(wroot, text="Abrir ventana modal", command=abrir_ventana_modal)
boton_modal.pack()

#Para mostrar un mensaje informativo

mbox.showinfo("Información", "Esto es un mensaje informativo.")

#Para crear un boton que nos deje elegir un atchivo

# Función para cargar un archivo
def cargar_archivo():
    archivo = filedialog.askopenfilename(filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")])
    if archivo:
        # Aquí puedes realizar acciones con el archivo, como mostrar su contenido o procesarlo
        print("Se seleccionó el archivo:", archivo)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Cargar Archivo")

# Crear un botón para cargar el archivo
boton_cargar = tk.Button(ventana, text="Cargar Archivo", command=cargar_archivo)
boton_cargar.pack()

wroot.mainloop()

