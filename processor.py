import PyPDF2 as pf

#Metodo para processar la lista de strings de prodcuto
def processText(p):
    p.insert(0,p[0][0])
    p[1] = p[1][1:]
    for i in range(0,len(p)):
        p[i] = p[i].replace(',','.')
    return p

def processLine(precio,pr):
    #Realizamos un bucle for para recorrer la lista de producto y generar solo los campos necesarios
    #uniendolos segun el patron  para dejar solo los campos necesarios
    while (True):
        if precio.search(pr[1]):
            if len(pr) == 2:
                pr.insert(1,pr[1])
            break
        else:
            pr[0] += ' '+pr[1]
            pr.pop(1)
    return pr

#Metodo para extraer la fecha del fichero
def processDate(data):
    date = str(data)
    date = date.split()
    date = date[0]
    date = date.replace('-','/')
    return date

        