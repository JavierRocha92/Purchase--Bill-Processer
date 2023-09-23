import PyPDF2 as pf
import processor as proc
import BBDD as bd
import re
def extractTextPDF(path):
    #Abrimos el fichero con la libreria pypdf
    pdf_obj = open(path,'rb')
    #Gaurdamos en un variable el objeto reader y le pasamos el objet pdf que hemos creado antes
    pdf_reader = pf.PdfReader(pdf_obj)
    #vamos a decirle que pagina queremos que lea del fichero pdf
    page_obj = pdf_reader.pages[0]
    #creamos una variable text para guatrdar el texto
    return page_obj.extract_text()

def extractDataPurchase(lines):
    #Vamos a quedarnos solo con la linea donde aparece el codigo de la compra, y realizamos un split para quedarnos con la fecha y el codigo de compra
    dates = lines[4].split()
    
    return proc.processDate(dates[0]),dates[1],dates[3]
    
#Metodo para extraeer los articulos de el texto dado como parametro

def extractArticles(lines,code):

    #Esta expresion regular nos incidica el final d la busqueda, ya que no empieza por un numero,
    #la fila que queremos dejar de leer
    start = re.compile(r'\d')

    #esta re la vamos a usar para el split cuando creamos la vaiable producto para separar en strings
    # los valores y crear una lista
    precio = re.compile(r'^\d+,\d\d')

    #Creamos las variable que nos hacen falta para procesar el texto del fichero PDF
    weight = False
    products = []
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
                """ EN ESTE CASO ESTAMOS PROCESANDO UN ARTICULO SIN PESO """
                #Vamos a ver si la varible weight esta o en True

                if weight == True:
                    #Vamos a hacer un extend de la variable aux con el pr que estamos procesando en esta iteracion

                    aux.extend(pr)
                    #Guardamos en la varible pr la variable aux una vez despues del extend

                    pr = aux

                #Llamamos al metodo para obtener la linea de datos procesada segun sus campos, le pasamos como parametrola re de precio
                #y el producto que vamos a procesar, y lo guardamos en la variable de product
                
                product,weight = proc.processLine(precio,pr,weight)
                article = proc.processText(product)
                #Le añadimos el codigo de la compra
                article.insert(0,code)
                products.append(article)
                
            else:
                #Si la longitud del producto es de 1 esto indca que es una articulo con peso
                weight = True
                #Guardamos en una variable auxiliar el producto de esta iteracion para procesarlo despues
                aux = pr
        else:
            #Aqui vamos a extraer el total de la compra para devolverlo tambien en la funcion
            
            break
#Devolvemos un lista de listas cons los datos de los diferentes articulos para insertarlos en la base de datos
    return products

#Metodo para extraer el precio total de los articulos de la lista

def extractPrice(articles):
    sum = 0
    for article in articles:
        sum += float(article[5])
    return round(sum,2)