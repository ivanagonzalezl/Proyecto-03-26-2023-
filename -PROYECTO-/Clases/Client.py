class Client():
    def __init__(self, name, dni, age, race, ondulado, n_ticket, validado, race_dni):

        self.name=name
        self.dni=dni
        self.age=age
        self.race=race
        self.ondulado=ondulado
        self.n_ticket=n_ticket
        self.validado=validado
        self.race_dni=race_dni

    def calculate_total(self):
        pass

    def show_attr(self):
        print(f"""
Nombre: {self.name}
Cédula: {self.dni}
Edad: {self.age}
Carrera: {self.race}
Validado: {self.validado}

""")