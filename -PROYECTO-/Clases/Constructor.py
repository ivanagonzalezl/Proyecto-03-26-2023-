class Constructor():

    def __init__(self, constructor_name, constructor_id, constructor_nationality, constructor_pilots):

        self.constructor_name= constructor_name
        self.constructor_id= constructor_id
        self.constructor_nationality= constructor_nationality
        self.constructor_pilots= constructor_pilots

    def show_attr(self):
        print (f"""
        Nombre: {self.constructor_name}
        ID del equipo: {self.constructor_id}
        Nacionalidad: {self.constructor_nationality}
        Pilotos: {self.constructor_pilots}
        """)
    

