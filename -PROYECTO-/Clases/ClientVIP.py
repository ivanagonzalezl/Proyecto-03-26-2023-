from Clases.Client import Client

class ClientVIP(Client):
    tipo="VIP"
    precio= 340
    
    def __init__(self, name, dni, age, race, ondulado, n_ticket, validado, race_dni):
        super().__init__(name, dni, age, race, ondulado, n_ticket, validado, race_dni)
        


    def calculate_total(self):
        if self.ondulado==True:
             self.total=(self.precio+(self.precio*0.16))-(self.precio*0.5)
        else:
             self.total=(self.precio+(self.precio*0.16))
        
        print(f"\nFACTURA\nAsientos: {self.n_ticket}.\n")
    
    def show_attr(self):
            print(f"""
Nombre: {self.name}
Cédula: {self.dni}
Edad: {self.age}
Carrera: {self.race}
Entrada: {self.tipo}
Validado: {self.validado}
""")
#TODO - PRECIOS. SE PUEDE COMPRAR MÁS DE UNA ENTRADA?