class Stock:
    def __init__(self):
        self.products_list = []

    def add_product(self, product):
        self.products_list.append(product)

    def update_stock(self, product, quantity):
        for prod in self.products_list:
            if prod.name == product.name:
                prod.update_quantity(quantity)

    def generate_alert(self, minimum_threshold):
        alerts = [
            prod.name
            for prod in self.products_list
            if prod.quantity < minimum_threshold
        ]

        return f"Productos por debajo del umbral: {", ".join(alerts)}" if alerts else "No hay ningún producto por debajo del umbral minimo designado"
