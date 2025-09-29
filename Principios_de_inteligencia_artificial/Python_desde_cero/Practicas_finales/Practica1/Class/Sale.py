from datetime import datetime 


class Sale:
    def __init__(self, client, products_list):
        self.client = client
        self.products_list = products_list
        self.date = datetime.now()
        self.total = self.calculate_total()

    def calculate_total(self):
        return sum(product.price for product in self.products_list)

    def register_sale(self):
        self.client.register_purchase(self)
        return f"Venta registrada {self.show_info()}"

    def show_info(self):
        products = ", ".join([product.name for product in self.products_list])
        return (
            f"Cliente: {self.client.name}, Productos: {products}, Total: {self.total}"
        )
