class Factura():

    def __init__(self, id, name, products, subtotal, perfect_id, discount, total):

        self.id=id
        self.name=name
        self.products= products
        self.subtotal= subtotal
        self.perfect_id= perfect_id
        self.discount= discount
        self.total= total
    
    def show_attr(self):

        print("""
        Nombre: {self.name}
        Cédula: {self.id}
        Productos: {self.products}
        Subtotal= {self.subtotal}
        Descuento= {self.discount}
        Total= {self.total}""")
        
