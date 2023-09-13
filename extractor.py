import PyPDF2 as pf
import processor as proc

def extractTextPDF(path):
    #Abrimos el fichero con la libreria pymupdf
    pdf_obj = open(path,'rb')
    #Gaurdamos en un variable el objeto reader y le pasamos el objet pdf que hemos creado antes
    pdf_reader = pf.PdfReader(pdf_obj)
    #vamos a decirle que pagina queremos que lea del fichero pdf
    page_obj = pdf_reader.pages[0]
    #creamos una variable text para guatrdar el texto
    return page_obj.extract_text()

def extractDate(path):
    #Abrimos el fichero con la libreria pymupdf
    pdf_obj = open(path,'rb')
    #Gaurdamos en un variable el objeto reader y le pasamos el objet pdf que hemos creado antes
    pdf_reader = pf.PdfReader(pdf_obj)
    #Llamamos a metodo para extraer la fecha de la metadata del fcihero
    date = pdf_reader.metadata.creation_date
    #Llamamos a metodo para procesar la variable data y retornarla en forma de string
    return proc.processDate(date)