class Product:
    def __init__(self, name, category, price, quantity):
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity

    def update_quantity(self, quantity):
        self.quantity = quantity

    def show_info(self):
        return f"Producto: {self.name}, Categoria: {self.category}, Precio: {self.price}, Cantidad: {self.quantity}"
    
