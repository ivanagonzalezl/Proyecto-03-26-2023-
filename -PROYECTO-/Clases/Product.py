class Product():
    def __init__(self, name, price, restaurant):

        self.name=name
        self.price=price
        self.restaurant=restaurant
    
    def show_attr(self):
        print(f"""
Nombre: {self.name}
Precio: {self.price}
Restaurant: {self.restaurant}""")