from AppMA import AppMA
from AppME import AppME


class App():

    def __init__(self):

        self.appa=AppMA()
        self.appe=AppME()

        self.appe.appMa = self.appa

    def start(self):
        self.appa.read_files()
        self.appe.from_txt_to_list()
        
        while True:

                option=input("""

BIENVENIDO F1 2023
1. Descargar información de las Api.
2. Gestión de Carreras y Equipos.
3. Gestion de Ventas de Entrada.
4. Gestion de Asistencia a las Carreras.
5. Gestion de Restaurantes.
6. Gestion de Venta de Restaurantes.
7. Indicadores de Gestión.
8. Salir\n>>> """) #FALTA TÍTULO
                
                print()
                if option=="1":
                    self.appa.down_load_data()
                    self.appe.donwload_api()
                elif option=="2":
                    self.appa.race_team_management()
                elif option=="3":
                    self.appa.regisgter()
                elif option=="4":
                    self.appa.attendance_ticket()
                elif option=="5":
                    self.appe.search_pro()
                elif option=="6":
                    self.appe.restaurant_management()
                elif option=="7":
                    self.appe.stats()
                elif option=="8":
                    print("Usted ha salido del programa.")
                    break
                else:
                    print("Ingreso inválido. Intente otra vez.")
                print()

