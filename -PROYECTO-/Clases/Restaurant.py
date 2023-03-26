class Restaurant():

    def __init__(self, nombre, race_name, products):

        self.nombre= nombre
        self.race_name= race_name
        self.products= products

    def show_attr(self):
        print("""
Nombre: {self.nombre}
Nombre de la carrera: {self.race_name}
Productos: {self.proudcts}""")
