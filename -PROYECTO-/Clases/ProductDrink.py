from Clases.Product import Product

class ProductDrink(Product):

    tipo="bebida"

    def __init__(self, name, price, restaurant, drink_type):
        super().__init__(name, price, restaurant)

        self.drink_type=drink_type
    
    def show_attr(self):
            print(f"""
Nombre: {self.name}
Precio: {self.price}
Restaurant: {self.restaurant}
Tipo de bebida: {"Alcohólica" if self.drink_type=="SI" else "No Alcohólica"}""")