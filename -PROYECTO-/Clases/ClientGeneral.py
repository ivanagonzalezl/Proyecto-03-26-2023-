from Clases.Client import Client

class ClientGeneral(Client):
    tipo="General"
    precio= 150
    
    def __init__(self, name, dni, age, race, ondulado, n_ticket, validado, race_dni):
        super().__init__(name, dni, age, race, ondulado, n_ticket, validado, race_dni)
    
    def calculate_total(self):
        if self.ondulado==True:
             self.total=(self.precio+(self.precio*0.16))-(self.precio*0.5)
        else:
             self.total=(self.precio+(self.precio*0.16))
    
    def show_attr(self):
            print(f"""
Nombre: {self.name}
Cédula: {self.dni}
Edad: {self.age}
Carrera: {self.race}
Entrada: {self.tipo}
Validado: {self.validado}
""")


