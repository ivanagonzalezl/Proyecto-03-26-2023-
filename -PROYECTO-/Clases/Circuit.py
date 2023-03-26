class Circuit:
    def __init__(self, circuit_name, circuit_country, circuit_locality, circuit_lat, circuit_long):

        self.circuit_name= circuit_name
        self.circuit_country= circuit_country
        self.circuit_locality= circuit_locality
        self.circuit_lat= circuit_lat
        self.circuit_long= circuit_long
    
    def show_attr(self):
        print (f"""
        Nombre: {self.circuit_name}
        País : {self.circuit_country}
        Localidad: {self.circuit_locality}
        Latitud: {self.circuit_lat}
        Longitud: {self.circuit_long}
        """)