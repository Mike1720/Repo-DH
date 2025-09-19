class Bank_Account:
    def __init__(self, titular, saldo_inicial):
        self.__titular = titular
        self.__saldo = saldo_inicial

    # SETTER - Establecer datos
    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"Deposito de {cantidad} exitoso")
        else:
            print("Error, la cantidad debe ser mayor a 0")

    def retirar(self, cantidad):
        if 0 < cantidad <= self.__saldo:
            self.__saldo -= cantidad
            print(f"Se ha retirado {cantidad} de tu saldo")
        elif cantidad <= 0:
            print("No se puede realizar la transacción")
        else:
            print("Saldo insuficiente")

    # GETTER - Obtener datos
    def get_saldo(self):
        return self.__saldo

