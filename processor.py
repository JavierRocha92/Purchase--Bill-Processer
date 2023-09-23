#Metodo para processar la lista de strings de prodcuto
def processText(p):
    #Insertamos en la posicion 0 el primer caracter de la posicion 0 y que indica las unidades del producto
    p.insert(0,p[0][0])
    #Ahora borramos la unidad de la posicion anterior que ahora pasa a ser la posicion 1
    p[1] = p[1][1:]
    #Recorremos la lista para borrar los caracteres que no queramos en el procesamiento
    for i in range(0,len(p)):
        p[i] = p[i].replace(',','.')
        p[i] = p[i].replace(' kg','')
    return p

def processLine(precio,pr,weight):
    #Realizamos un bucle for para recorrer la lista de producto y generar solo los campos necesarios
    #uniendolos segun el patron  para dejar solo los campos necesarios
    while (True):
        if weight == False:
            #buscamos si la segunds posicion de la lista contiene un precio
            if precio.search(pr[1]):
                #Si la lomgitud de la lista es de dos entonces
                if len(pr) == 2:
                    pr.insert(1,pr[1])
                if len(pr) == 3:
                #Si la longitud de la lista es de 3 entonces en la posicion 1 metemos un espacio en blanco para
                #que el peso del articulo no se quede nulo
                    pr.insert(1,'')
                break
            else:
                #Cuando no se encuentra la expresion regular pasamos a la posicion cero lo que ya tiene mas lo que hay en 
                #la posicion 1 para generar en una sola psocion el nombre el aerticulo
                pr[0] += ' '+pr[1]
                pr.pop(1)
        else :
            #Si es una fruta lo que hacemos es borrar los datos que no nos sirvan para el procesamiento
            pr.pop(2)
            pr.pop(3)
            weight = False
    return pr,weight

#Metodo para extraer la fecha del fichero
def processDate(data):
    date = str(data)
    date = date.split()
    date = date[0]
    date = date.replace('-','/')
    return date
