import requests
import os
from tabulate import tabulate
from Clases.Restaurant import Restaurant
from Clases.ProductDrink import ProductDrink as Drink
from Clases.ProductFood import ProductFood as Food
from Clases.ClientVIP import ClientVIP as Vip
from Clases.Factura import Factura


class AppME():
    def __init__(self):
        self.restaruants=[]
        self.clients=[]
        

        self.restaurants=[]
        self.foods=[]
        self.drinks=[]

        self.facturas=[]
        self.appMa = None

    def donwload_api(self):
        url_races='https://raw.githubusercontent.com/Algorimtos-y-Programacion-2223-2/api-proyecto/main/races.json'
        response_r=requests.request("GET", url_races)

        directory = os.getcwd()+"/TXT/Modulo IV/"
        file_name = "Restaurant.txt"
        with open(directory + file_name,"w") as f:
            for restaurant in response_r.json():
                res=restaurant["name"]
                for r in restaurant["restaurants"]:
                    x=''
                    y=r["name"]
                    for i in r["items"]:
                        c=i["name"]
                        x+=f"{c}-"
                    
                    f.write(f"{y}|{res}|{x}|\n")
        
        file_name = "ProductDrink.txt"
        with open(directory + file_name,"w") as f:
            for race in response_r.json():
                for restaurant in race["restaurants"]:
                    res=restaurant["name"]
                    for drink in restaurant["items"]:
                        if drink["type"]=="drink:alcoholic":
                            f.write(f'{drink["name"]}|{drink["price"]}|{res}|SI|\n')
                        elif drink["type"]=="drink:not-alcoholic":
                            f.write(f'{drink["name"]}|{drink["price"]}|{res}|NO|\n')

        file_name = "ProductFood.txt"
        with open(directory + file_name,"w") as f:
            for race in response_r.json():
                for restaurant in race["restaurants"]:
                    res=restaurant["name"]
                    for food in restaurant["items"]:
                        if food["type"]=="food:restaurant":
                            f.write(f'{food["name"]}|{food["price"]}|{res}|Restaurant|\n')
                        elif food["type"]=="food:fast":
                            f.write(f'{food["name"]}|{food["price"]}|{res}|Fast|\n')
                            
    def from_txt_to_list(self):
        directory= os.getcwd()+"/TXT/Modulo IV/"
        self.restaurants=[]
        file_name='Restaurant.txt'
        with open(directory+file_name) as f:
            for line in f:
                x=[]
                for producto in line.split("|")[2].split("-"):
                    x.append(producto)
                restaurant= Restaurant(line.split("|")[0],line.split("|")[1],x)
                self.restaurants.append(restaurant)
        

        self.drinks=[]
        file_name='ProductDrink.txt'
        with open(directory+file_name) as f:
            for line in f:
                drink= Drink((line.split("|")[0]).capitalize(),float(line.split("|")[1])+(float(line.split("|")[1])*0.16),line.split("|")[2],line.split("|")[3])
                self.drinks.append(drink)
    

        self.foods=[]
        file_name='ProductFood.txt'
        with open(directory+file_name) as f:
            for line in f:
                food= Food((line.split("|")[0]).capitalize(),float(line.split("|")[1])+(float(line.split("|")[1])*0.16),line.split("|")[2],line.split("|")[3])
                self.foods.append(food)

        directory=os.getcwd()+"/TXT/Modulo II/"
        self.clients=[]
        file_name="ClientVIP.txt"
        with open(directory+file_name) as f:
            for line in f:
                name=line.split(",")[0]
                dni=int(line.split(",")[1])
                age=int(line.split(",")[2])
                race=line.split(",")[3]
                ondulado=line.split(",")[4]
                n_ticket=int(line.split(",")[5])
                validado=line.split(",")[6] 
                validado=True if validado=="True" else False
                race_id=int(line.split(",")[7])

                cliente_vip= Vip(name, dni, age, race, ondulado, n_ticket, validado, race_id)
                self.clients.append(cliente_vip)
        
        self.facturas= []
        directory=os.getcwd()+"/TXT/Modulo V/"
        file_name="Factura.txt"
        with open(directory+file_name) as f:
            for line in f:
                x=[]
                for producto in line.split("|")[2].split("-"):
                    x.append(producto)
                
                factura= Factura(int(line.split("|")[0]),line.split("|")[1],x,float(line.split("|")[3]),line.split("|")[4],float(line.split("|")[5]),float(line.split("|")[6]))
                self.facturas.append(factura)
        
        for factura in self.facturas:
            for i in factura.products:
                if "" in factura.products:
                    factura.products.remove("")


    #MODULO 4
    def search_pro_name(self):
        print("\nBÚSQUEDA POR NOMBRE DE PRODUCTO🔍")
        restaurantes=[]
        for restaurant in self.restaurants:
            restaurantes.append(restaurant.nombre)
        print('')
        for i, restaurant in enumerate(restaurantes):
            print(f"{i+1}. {restaurant}")
        print('')
        while True:
            try:
                op=int(input("Ingrese el número del restaruante que desea ver: "))
                while op not in range(1,len(restaurantes)+1):
                    raise Exception
                break
            except: 
                print("Ingreso inválido, intente nuevamente: ")

        r=restaurantes[op-1]
        productos=[]
        for alimento in self.foods:
            if r==alimento.restaurant:
                productos.append(alimento)
        
        for bebida in self.drinks:
            if r==bebida.restaurant:
                productos.append(bebida)
        
        for i, product in enumerate(productos):
            print(f"{i+1}. {product.name}")
        
        option=input('\nSeleccione el producto que desea visualizar: ')
        while not option.isnumeric() or int(option) not in range(1,len(productos)+1):
            option=input("Error: ingreso inválido, intente nuevamente.")
        
        productos[int(option)-1].show_attr()
        
    def search_pro_type(self):
        print("\nBÚSQUEDA POR TIPO DE PRODUCTO🔍🍴")
        alcoholica=[]
        no_alcoholica=[]
        restaurant=[]
        fast=[]

        for drink in self.drinks:
            if drink.drink_type=="SI":
                alcoholica.append(drink)
            elif drink.drink_type=="NO":
                no_alcoholica.append(drink)
        
        for food in self.foods:
            if food.food_type=="Restaurant":
                restaurant.append(food)
            elif food.food_type=="Fast":
                fast.append(food)
        
        print("\nEscoja el tipo de producto que desea ver:")
        option=input("1.Bebidas.\n2.Alimentos.\n>>> ")

        while option!="1" and option!="2":
            option=input("Ingreso inválido, intente nuevamente: ")
        
        if option=="1":
            print("Escoja el tipo de bebida que desea visualizar: ")
            option_b=input("\n1.Alcohólicas.\n2.No alcohólicas.\n>>> ")
            while option_b!="1" and option_b!="2":
                option_b=input("Ingreso inválido, intente nuevamente: ")
            print('')
            if option_b=="1":
                print("Bebidas Alcohólicas🍸🥂")
                for i, drink in enumerate(alcoholica):
                    print(f"{i+1}. {drink.name}")

                while True:
                    try:
                        option_c=int(input("Seleccione la bebida que desea visualizar: "))
                        while option_c not in range(1,len(alcoholica)+1):
                            raise Exception
                        break
                    except:
                        print("Ingreso inválido, intente nuevamente: ")

                alcoholica[option_c-1].show_attr()

            if option_b=="2":
                print("Bebidas no alcohólicas🧃🥤")
                for i, drink in enumerate(no_alcoholica):
                        print(f"{i+1}. {drink.name}")

                while True:
                    try:
                        option_c=int(input("Seleccione la bebida que desea visualizar: "))
                        while option_c not in range(1,len(no_alcoholica)+1):
                            raise Exception
                        break
                    except:
                        print("Ingreso inválido, intente nuevamente: ")

                no_alcoholica[option_c-1].show_attr()

        if option=="2":
            print("Escoja el tipo de alimento que desea visualizar: ")
            option_b=input("\n1.Restaurant.\n2.Fast.\n>>> ")

            while option_b!="1" and option_b!="2":
                option_b=input("Ingreso inválido, intente nuevamente. ")

            if option_b=="1":
                print("Alimentos Empaquetados🍽️ ")
                for i, food in enumerate(restaurant):
                    print(f"{i+1}. {food.name}")

                while True:
                    try:
                        option_c=int(input("Seleccione la bebida que desea visualizar: "))
                        while option_c not in range(1,len(restaurant)+1):
                            raise Exception
                        break
                    except:
                        print("Ingreso inválido, intente nuevamente: ")

                restaurant[option_c-1].show_attr()
            
            if option_b=="2":
                print("Alimentos para llevar. 🍔🍟")
                for i, food in enumerate(fast):
                    print(f"{i+1}. {food.name}")

                while True:
                    try:
                        option_c=int(input("Seleccione la bebida que desea visualizar: "))
                        while option_c not in range(1,len(fast)+1):
                            raise Exception
                        break
                    except:
                        print("Ingreso inválido, intente nuevamente: ")

                fast[option_c-1].show_attr()

        
    def search_pro_range(self):
        print("BÚSQUEDA DE PRODUCTOS POR RANGO DE PRECIO🔍🧮")
        print("")
        productos=[]

        for alimento in self.foods:
            productos.append(alimento)
        for bebida in self.drinks:
            productos.append(bebida)

        while True:
            try:
                num_1=float(input("Ingrese el primer número del rango de precios en el que desea buscar: "))
                while num_1<0:
                    print("No tenemos productos con precios tan bajos.")
                    raise Exception
                num_2=float(input("Ingrese el segundo número del rango de precios en el que desea buscar: "))
                while num_2<num_1:
                    print("\nEl segundo número debe ser mayor al primero")
                    raise Exception
                break
            except:
                print("Ingreso inválido, intente de nuevo. ")
                print("")
        print("")
        products_on_range=[]
        exists = False
        print("Productos en el rango seleccionado")
        for producto in productos:
            if producto.price>num_1 and producto.price<num_2:
                products_on_range.append(producto)
                exists  = True
        if not exists:
            print("No hay existen productos en ese rango de precio")
        
        if len(products_on_range)!=0:
            for i, producto in enumerate(products_on_range):
                print(f"{i+1}. {producto.name}")
            
            op=input("\nSeleccione el producto que desea ver: ")
            while not op.isnumeric() or int(op) not in range(1,len(products_on_range)+1):
                op=input("Ingreso inválido, intente nuevamente.")

            products_on_range[int(op)-1].show_attr()


    def search_pro(self):
        while True:
            print("\n🧑‍🍳 BUSQUEDA DE PRODUCTOS DE LOS RESTAURANTES 🧑‍🍳\n")
            option=input("1.Búsqueda de productos por nombre.\n2.Búsqueda de productos por tipo.\n3.Búsqueda de productos por rango de precio.\n4.Volver.\n>>> ")

            while not option.isnumeric() or int(option) not in range(1,5):
                option=input("Ingreso inválido, intente nuevamente: ")
            
            if option=="1":
                self.search_pro_name()
            elif option=="2":
                self.search_pro_type()
            elif option=="3":
                self.search_pro_range()
            elif option=="4":
                break

#MODULO 5

    def restaurant_management(self):
        print("🥓🍖MODULO DE VENTA DE RESTAURANTES🍖🥓")
        print("")
        for restaurant in self.restaruants:
            print(restaurant)

        dni=input("Ingrese su cedula: ")
        while not dni.isnumeric():
            dni=input("Ingreso no valido, intente de nuevo: ")
        
        client_ = None
        for client in self.clients:
            if int(dni)==client.dni:
                client_=client
                break
        
        if client_==None:
            print("No se encontró en la lista de clientes VIP")
            return

        print(client_.race)
        products=[]

        restaurant_=None
        for restaurant in self.restaurants:
            if client_.race==restaurant.race_name:
                restaurant_=restaurant
                break
        if restaurant_==None:
            print("No se encontró el restaurante.")

        for food in self.foods:
            if restaurant_.nombre==food.restaurant:
                products.append(food)
        
        
        for drink in self.drinks:
            if restaurant_.nombre==drink.restaurant:
                if client_.age<18 and drink.drink_type=="NO":
                    products.append(drink)

        print("")  
        for i, producto in enumerate(products):
            print(f"{i+1}. {producto.name}: ${producto.price}")
        
        print("")
        continuar=input("¿Dese agregar un producto a su carrito?: \n1.Si.\n2.No.\n>>> ")
        while continuar!="1" and continuar!="2":
            continuar=input("Ingrese una de las opciones numéricas indicadas: ")
        

        car=[]
        costos=[]
        while continuar=="1":

            op=input("Ingrese el producto que desea: ")
            while not op.isnumeric() or int(op) not in range(1,len(products)+1):
                op=input("Esa opción de producto no existe: ")
            
            producto=products[int(op)-1]
            costos.append(producto.price)

            car.append(producto)


            continuar=input("\n¿Dese agregar otro producto a su carrito?\n1.Si.\n2.No.\n>>> ")
            while continuar!="1" and continuar!="2":
                continuar=input("Ingrese una de las opciones numéricas indicadas: ")

        
        #NUMERO PERFECTO
        divisores=[]
        dni=int(dni)
        descuento = 0

        for n in range(1, (dni)):
            if dni%n==0:
                divisores.append(n)
        
        if sum(divisores)==dni:
            perfecto=True
        else:
            perfecto=False
        
        #SUBTOTAL
        subtotal=sum(costos)

        #DESCUENTO
        if perfecto==True:
            descuento=subtotal*0.15
        
        #TOTAL
        total=subtotal-(descuento)
        print("")
        print("TOTAL")
        for i, product in enumerate(car):
            print(f"{i+1}. {product.name}")
        print("")
        print(f"SUBTOTAL={round(subtotal,2)}\nDESCUENTO={round(descuento,2)}\nTOTAL= {round(total,2)}")

        proceder=input('\n¿Dese proceder con su compra?\n1.Si\n2.No.\n>>> ')
        while proceder!="1" and proceder!="2":
            proceder=input('Ingrese un valor numérico de las opciones: ')
        
        if proceder=="1":
            print("")
            print("PAGO EXITOSO✅")
            print("Resumen de compra:")
            for i, product in enumerate(car):
                print(f"{i+1}. {product.name} {product.price}")
            print("")
            print(f"SUBTOTAL={round(subtotal,2)}\nDESCUENTO={round(descuento,2)}\nTOTAL= {round(total,2)}")

            
        
        car_=[]
        for producto in car:
            car_.append(producto.name)
        

        factura= Factura(dni,client_.name,car_,round(subtotal,2),perfecto,round(descuento,2),round(total,2))
        self.facturas.append(factura)


        directory= os.getcwd()+"/TXT/MODULO V/"
        file_name="Factura.txt"
        with open (directory+file_name,'w') as f:
            for factura in self.facturas:
                x=''
                for producto in factura.products:
                    x+=f"{producto}-"
                f.write(f"{factura.id}|{factura.name}|{x}|{factura.subtotal}|{factura.perfect_id}|{factura.discount}|{factura.total}|\n")
        


# MODULO 6
    def get_tabla(self):
        print("")
        print("")
        print("TABLA DE ASISTENCIA A LAS CARRERAS")
        print("")
        carreras = {}
        tabulate.PRESERVE_WHITESPACE = True
        tabulate.WIDE_CHARS_MODE = False

        for client in self.appMa.general:
            if carreras.get(client.race) == None:
                carreras[client.race] = {
                    "total comprado": 1, 
                    "total asistido": 0 if client.validado == False else 1
                    }
            else:
                carreras[client.race]["total comprado"] += 1
                carreras[client.race]["total asistido"] +=  0 if client.validado == False else 1

        for client in self.appMa.vip:
                if carreras.get(client.race) == None:
                    carreras[client.race] = {
                        "total comprado": 1, 
                        "total asistido": 0 if client.validado == False else 1
                        }
                else:
                    carreras[client.race]["total comprado"] += 1
                    carreras[client.race]["total asistido"] +=  0 if client.validado == False else 1

        for i, carrera in carreras.items():
            if carrera.get("a/v") == None:
                carreras[i]["a/v"]= round(((carreras[i]["total asistido"]*100)/carreras[i]["total comprado"]),1) if carreras[i]["total comprado"]>0 else "0.0%"

        for race in self.appMa.races:
            for i, carrera in carreras.items():
                if carrera.get("circuito") == None:
                    if race.race_name==i:
                        carreras[i]["circuito"]=race.race_circuit

        carreras_sorted=[]
        for carrera in sorted(carreras, key= lambda carrera: carreras[carrera]["a/v"], reverse=True):
            x=[]
            x.append(carrera)           
            x.append(carreras[carrera]["circuito"])
            x.append(carreras[carrera]["total comprado"])
            x.append(carreras[carrera]["total asistido"])
            x.append(f'{carreras[carrera]["a/v"]}%')
             
            carreras_sorted.append(x)
        
        print(tabulate(carreras_sorted, headers=["  🏁CARRERA🏁  ","  🚩CIRCUITO🚩  ","  🎫BOLETOS VENDIDOS🎫  ","  🙋ASISTENCIA🙋  ","  📈RELACIÓN A/V📉  "],tablefmt="pretty"))
        print("")
        print("")


    def max_attendance(self):

        carreras = {}
        for client in self.appMa.general:
            if carreras.get(client.race) == None:
                carreras[client.race] = {
                    "total comprado": 1, 
                    "total asistido": 0 if client.validado == False else 1
                    }
            else:
                carreras[client.race]["total comprado"] += 1
                carreras[client.race]["total asistido"] +=  0 if client.validado == False else 1

        for client in self.appMa.vip:
                if carreras.get(client.race) == None:
                    carreras[client.race] = {
                        "total comprado": 1, 
                        "total asistido": 0 if client.validado == False else 1
                        }
                else:
                    carreras[client.race]["total comprado"] += 1
                    carreras[client.race]["total asistido"] +=  0 if client.validado == False else 1
        
        for i, carrera in carreras.items():
            if carrera.get("a/v") == None:
                carreras[i]["a/v"]= round(((carreras[i]["total asistido"]*100)/carreras[i]["total comprado"]),2) if carreras[i]["total comprado"]>0 else 0.0

        for carrera in sorted(carreras, key= lambda carrera: carreras[carrera]["total asistido"]):
            carrera_max= f'La carrera con más asistencias es {carrera}, con un total de {carreras[carrera]["total asistido"]} asistencias.'
        
        print(carrera_max)
    
    def max_sell(self):

        carreras = {}
        for client in self.appMa.general:
            if carreras.get(client.race) == None:
                carreras[client.race] = {
                    "total comprado": 1, 
                    "total asistido": 0 if client.validado == False else 1
                    }
            else:
                carreras[client.race]["total comprado"] += 1
                carreras[client.race]["total asistido"] +=  0 if client.validado == False else 1

        for client in self.appMa.vip:
                if carreras.get(client.race) == None:
                    carreras[client.race] = {
                        "total comprado": 1, 
                        "total asistido": 0 if client.validado == False else 1
                        }
                else:
                    carreras[client.race]["total comprado"] += 1
                    carreras[client.race]["total asistido"] +=  0 if client.validado == False else 1
        
        for i, carrera in carreras.items():
            if carrera.get("a/v") == None:
                carreras[i]["a/v"]= round(((carreras[i]["total asistido"]*100)/carreras[i]["total comprado"]),2) if carreras[i]["total comprado"]>0 else 0.0

        for carrera in sorted(carreras, key= lambda carrera: carreras[carrera]["total comprado"]):
            carrera_max= f'La carrera con mayor venta de boletos es {carrera}, con un total de {carreras[carrera]["total comprado"]} de boletos vendidos.'
        
        print(carrera_max)
    
    def average_expense(self):

        gastos={}
        g=[]
        
        
        for factura in self.facturas:
            if gastos.get(factura.id) == None:
                gastos[factura.id] = factura.total+340
            else:
                gastos[factura.id]+= factura.total
        
        for i, gasto in gastos.items():
            g.append(gasto)
        
        promedio= sum(g)/len(g)
        
        print("")
        print(f"El promedio de gastos de un cliente VIP es de: {round(promedio,2)}")
        print("")

    def top_restaurant(self):
        print("\n📠TOP 3 PRODUCTOS MÁS VENDIDOS📠\n")

        productos={}
        
        for factura in self.facturas:
            for producto in factura.products:
                if productos.get(producto) == None:
                    productos[producto] = {"cantidad":1,
                                           "nombre": producto}
                else:
                    productos[producto]["cantidad"]+= 1
        
        top_productos=[]
        for producto in sorted(productos, key= lambda producto: productos[producto]["cantidad"], reverse=True):
            x=[]
            x.append(producto)
            x.append(productos[producto]["cantidad"])

            top_productos.append(x)

        top_productos=top_productos[0:3]

        for i, x in enumerate(top_productos):
            print(f'{i+1}. {(x[0]).title()}: {x[1]} ventas.')


    def top_clients(self):
        print("\n🎟️ 🔝 TOP 3 CLIENTES QUE MÁS BOLETOS COMPRARON 🔝🎟️\n")

        clients = {}

        for client in self.appMa.general:
            if clients.get(client.dni) == None:
                clients[client.dni] = {
                    "boletos comprados": 1, 
                    "nombre": client.name
                    }
            else:
                clients[client.dni]["boletos comprados"] += 1
        
        for client in self.appMa.vip:
            if clients.get(client.dni) == None:
                    clients[client.dni] = {
                    "boletos comprados": 1, 
                    "nombre": client.name
                    }
            else:
                [client.dni]["boletos comprados"] += 1
        
        top_clients=[]
        for client in sorted(clients, key= lambda client: clients[client]["boletos comprados"], reverse=True):
            x=[]
            x.append(clients[client]["nombre"])
            x.append(clients[client]["boletos comprados"])


            top_clients.append(x)

        top_clients=top_clients[0:3]

        for i, x in enumerate(top_clients):
            print(f'{i+1}. {(x[0]).title()}: {x[1]} boleto(s) comprado(s).')
        
    def stats(self):
        print("📈📉 ESTADÍSTICAS 📈📉")
        while True:
            op=input("""
1. Promedio de gastos de un cliente VIP.
2. Tabla de asistencias
3. Carrera con mayor asistencia.
4. Carrera con mayor venta de boletos.
5. Top 3 productos más vendidos en el restaurante.
6. Top 3 clientes que más compraron boletos.
7. Salir.
>>> """)

            while not op.isnumeric() or not int(op) in range(1,8):
                op=input("Ingrese una de las opciones numéricas anterioremente mostradas: ")
            if op=="1":
                self.average_expense()
            if op=="2":
                self.get_tabla()
            if op=="3":
                self.max_attendance()
            if op=="4":
                self.max_sell()
            if op=="5":
                self.top_restaurant()
            if op=="6":
                self.top_clients()
            if op=="7":
                break
