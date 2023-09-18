import PyPDF2 as pf
import processor as proc

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
    
    



