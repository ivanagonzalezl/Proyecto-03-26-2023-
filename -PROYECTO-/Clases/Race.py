class Race():
    def __init__(self, race_name, race_number, race_date, race_circuit, race_podium, race_end):

        self.race_name= race_name
        self.race_number= race_number
        self.race_date= race_date
        self.race_circuit= race_circuit
        self.race_podium= race_podium
        self.race_end= race_end

    
    def show_attr(self):

        print (f"""
        Nombre: {self.race_name}
        Número de carrera: {self.race_number}
        Fecha de la carrera: {self.race_date}
        Circuito: {self.race_circuit}
        Finalizada= {self.race_end}
        Podium:
        {self.race_podium}
        """)
    ###PODIUM
    ###END