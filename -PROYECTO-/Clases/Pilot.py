class Pilot():

    def __init__(self,pilot_name, pilot_last_name, pilot_birth_date, pilot_birth_place, pilot_number, pilot_team):

        self.pilot_name= pilot_name
        self.pilot_last_name= pilot_last_name
        self.pilot_birth_date= pilot_birth_date
        self.pilot_birth_place= pilot_birth_place
        self.pilot_number= pilot_number
        self.pilot_team= pilot_team
    
    def show_attr(self):
        print (f"""
        Nombre: {self.pilot_name}
        Apellido: {self.pilot_last_name}
        Fecha de Nacimiento: {self.pilot_birth_date}
        Lugar de Nacimiento: {self.pilot_birth_place}
        Número: {self.pilot_number}
        Equipo: {self.pilot_team}
        """)