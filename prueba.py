from Product import Product
p = Product(1,'camiseta',1.33,2.00)
print(p)

cadenas =['1,22','3,44','5,77']
for cadena in cadenas:
    cadena = lambda cadena : cadena.replace(',','.')
    
print(cadenas)