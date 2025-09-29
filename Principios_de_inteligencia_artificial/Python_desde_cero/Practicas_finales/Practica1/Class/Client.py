class Client:
    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone
        self.purchase_history = []

    def update_info(self, address=None, phone=None):
        if address:
            self.address = address
        elif phone:
            self.phone = phone

    def register_purchase(self, purchase):
        self.purchase_history.append(purchase)

    def get_info(self):
        return f"Nombre del cliente: {self.name}, Dirección: {self.address}, Telefono {self.phone}"
    
