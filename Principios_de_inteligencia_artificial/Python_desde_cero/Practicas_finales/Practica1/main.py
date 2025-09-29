# Funciones principales de la interfaz de consola
from Class.Sale import Sale
from Class.Product import Product
from Class.Stock import Stock
from Class.Client import Client
from Class.Pet import Cat, Dog


def register_pet():
    type_of_pet = input("Ingrese el tipo de mascota (Perro/Gato): ").strip().lower()
    name = input("Nombre de la mascota: ")
    age = int(input("Edad de la mascota: "))
    health = input("Estado de salud de la mascota: ")
    price = float(input("Precio de la consulta: "))

    if type_of_pet == "perro":
        breed = input("Raza del perro: ")
        energy_level = input("Nivel de energia del perro: ")
        pet = Dog(name, age, health, price, breed, energy_level)
    elif type_of_pet == "gato":
        breed = input("Raza del gato: ")
        independence = input("Nivel de independencia del gato: ")
        pet = Cat(name, age, health, price, breed, independence)
    else:
        print("Tipo de mascota no reconocido")
        return
    return pet


def register_client():
    name = input("Nombre del cliente: ")
    address = input("Dirección: ")
    phone = input("Telefono: ")
    client = Client(name, address, phone)
    return client


def register_product():
    name = input("Nombre del producto: ")
    category = input("Categoria del producto: ")
    price = float(input("Costo del producto: "))
    quantity = int(input("Cantidad de producto: "))
    product = Product(name, category, price, quantity)
    return product


def register_sale(clients, stock):
    name_client = input("Nombre del cliente: ")
    client = next((c for c in clients if c.name == name_client), None)
    if not client:
        print("Cliente no encontrado")
        return

    products = []

    while True:
        product_name = input(
            "Ingrese nombre del producto (Deje vacio para finalizar): "
        )
        if not product_name:
            break
        product = next((p for p in stock.products_list if p.name == product_name), None)
        if product:
            products.append(product)
        else:
            print("Producto no encontrado")

    if products:
        sale = Sale(client, products)
        sale.register_sale()
        print("La venta ha sido registrada")
    else:
        print("No se ha registrado ningún producto")


def show_menu():
    print("\n --- Menú de gestión de Patas Felices")
    print("1.- Registrar Mascota")
    print("2.- Registrar Cliente")
    print("3.- Registrar Producto")
    print("4.- Registrar Venta")
    print("5.- Mostrar información acerca de Mascotas")
    print("6.- Mostrar información acerca de Clientes")
    print("7.- Mostrar información acerca de Productos")
    print("8.- Generar alerta de inventario")
    print("9.- Salir")


def main():
    pets = []
    clients = []
    stock = Stock()

    while True:
        show_menu()
        option = input("Seleccione una opcion: ")

        if option == "1":
            pet = register_pet()
            if pet:
                pets.append(pet)
                print("Mascota registrada con éxito")
        elif option == "2":
            client = register_client()
            if client:
                clients.append(client)
                print("Cliente registrado con éxito")
        elif option == "3":
            product = register_product()
            if product:
                stock.add_product(product)
                print("Producto registrado con éxito")
        elif option == "4":
            register_sale(clients, stock)
        elif option == "5":
            for pet in pets:
                print(pet.get_info())
                if isinstance(pet, Dog) or isinstance(pet, Cat):
                    print(pet.show_characteristics())
        elif option == "6":
            for client in clients:
                print(client.get_info())
        elif option == "7":
            for prodcut in stock.products_list:
                print(prodcut.show_info())
        elif option == "8":
            minimum_threshold = int(input("Ingrese el umbral mínimo del inventario: "))
            print(stock.generate_alert(minimum_threshold))
        elif option == "9":
            print("Saliendo del sistema ¡Gracias por usar Patas Felices App!")
            break
        else:
            print("Opción invalida")


if __name__ == "__main__":
    main()
