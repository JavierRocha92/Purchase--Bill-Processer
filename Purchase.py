#Creamos una clase de compras para almacenar los productos realizados en una misma
# compra por grupos y poder operar con ellos

class Purchase(object):
    products = []
    def __init__(self,date,total_product = None,total_price = None):
        """ Constructor e la clase Purchase """
        self.date = date
        self.total_product = total_product
        self.total_price = total_price
        
    def findExpensive(self):
        """ Este metodo develve el producto que mas cuesta en su precio por unidad """
        #Ordenamos la lista de productos segun el parametro de ud_price
        sorted(self.products, key= lambda products : self.products.ud_price)
        return self.products[0]
    
    def findMostSpend(self):
        """ Este metodo devuelve el producto en el que mas inero se ha gastado en la compra """
        #Ordenamos la lista de productos segun el parametro de ud_price
        sorted(self.products, key= lambda products : self.products.price)
        return self.products[0]
        
    def addProduct(self,p):
        """ Agrega al objeto Purchase un nuevo Product """
        self.products.append(p)

    def __str__(self):
        return f'Date: {self.date} total items : {self.total_product} total price : {self.total_price}'
    
    def setTotalPrice(self):
        total = 0.0
        for product in self.products:
            total += float(product.price)
        total = round(total,2)
        return total
