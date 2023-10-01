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

# metodo para procesar la fecha que extraemos del pdf para realizar una inserccion

def extractDataPurchase(lines):
    #Vamos a quedarnos solo con la linea donde aparece el codigo de la compra, y realizamos un split para quedarnos con la fecha y el codigo de compra
    dates = lines[4].split()
    # Vamos a guardar la fecha de la compra en formato iso con lo cual llamamos a metodo para procesarla
    
    return proc.processDateInsert(dates[0],dates[1]),dates[3]

    
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
            if  len(pr) > 1 and precio.search(pr[-1]):
                """ AQUI ESTA EL ERROR YA QUE SI UNA FRUTA TIENE UN NOMBRE COMPUESTO ENTTRAARA DIRECTAMENTE EN ESTE IF
                SIN TENER EL PESO EN TRUE HAY QUE CAMBIAR LA CONDICION"""
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
                #Llamamos a metodo para evitar tener articulos repetidos en la lista
                mergeEqualArticles(products)
                
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

#Metodo para sumar las unidades , pesos y precios de los articulos repetidos en la lista

def mergeEqualArticles(articles):
    if(len(articles) > 1):
        #Recorremos la lista de articulos menos la ultimos posicion para buscar concurrencias del nombre 
        # de este ultimo elemento en la lista para realizar la operacion de fusion
        for i in range(0,len(articles)- 1):
            last = articles[len(articles)- 1]
            #Condicional para saber si el nombre del elemento de la lista coincide con el de el ultimo elemento, en este caso
            #seria el ultimo elemento insertado
            if(articles[i][2] == last[2]):
                #Si encontramos la ocncurrencia vamos a sumar el peso, el precio, y las unidades de ambos y el ultimo elemento
                #y el ultimo elemento lo borraremos, simulamdo asi una fusion,las unidades solo las sumaremos cuando el elemento
                #no tenga peso ya que si es asi es un elemento contable

                """AHORA VAMOS A CAPTURAR UNA EXCEPCION SI AL PASAR EL SIGUIENTE DATO DEL ARTICULO (WEITGHT) A TIPO FLOAT CON 
                LA EXCEPCION ValueError QUE SE DARA CUANDO EL ELEMENTO PESO ESTE VACIO, ESTO NOS INDICARA QUE EL ELEMENTO QUE SE
                ESTA REPITIENDO NO ES UN ARTICULO CON PESO Y DEBEREMOS HACER OTRAS OPERACIONES DIFERENTES"""
                
                #Primero vamos a sumar los precios totales ya que aunque salte la excepcion o no la operacion
                #con el precio va a ser la misma
                
                articles[i][5] = str(round(float(articles[i][5]) + float(last[5]),2))
                try:

                    #Intentamos hacer un casting del siguiente elemento de la lista (weight) a float para ver si nos salta la excepcion
                    articles[i][3] = str(float(articles[i][3]) + float(last[3]))
                    print('no salta la exceepcion')

                except ValueError as e:
                    
                    """PRIMERO INCREMENTAMOS LAS UNIDADES, HACEMOS LA OPERACION PASANDO LOS DATOS A TIPO INT Y LOS DEVOLVEMOS UNA VEZ
                    INCREMENTADOS COMO TIPO STRING"""
                    articles[i][1] = str(int(articles[i][1]) + 1)
                    
                    #Si salta la excepcion es porque el elemento de la lista no tiene peso asique vamos a hacer la media de el precio
                    #por unidad de el articulo
                    
                    """LA OPERACION QUE REALIZAMOS ES INSERTAR EN EL PRECIO POR UNIDAD LA DIVISION DEL PRECIO TOTAL POR EL NUERMO
                    DE UNIDADES (LA MEDIA DE UN SUMATORIO)"""
                    
                    articles[i][4] = str(round(float(articles[i][5]) / int(articles[i][1]),2))
                    
                #Cuando ya tenemos los articulos fusionados pasamos a borrar el ultimo elemento de la lista asi eliminamos
                #la concurrencia de elemeneto en la lista
                
                articles.pop()
                
                #Al realizar las operacion utilizamos la sentencia break para salirnos del bucle ya que  no puede haber mas de dos 
                #elementos iguales
                
                break    
            