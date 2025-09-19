from Class.Bank_account import Bank_Account

cuenta = Bank_Account("Miguel", 100)

# print(cuenta.__saldo) # Error
print(cuenta.get_saldo()) # Output: 100

cuenta.retirar(150) # Output: Saldo insuficiente
cuenta.depositar(50) # Output: Deposito de 50 exitoso
cuenta.retirar(150) # Output: Se ha retirado 150 de tu saldo
cuenta.depositar(20) # Output: Deposito de 20 exitoso
cuenta.depositar(0) # Output: Error, la cantidad debe ser mayor a 0
cuenta.retirar(0) # Output: No se puede realizar la transacción

