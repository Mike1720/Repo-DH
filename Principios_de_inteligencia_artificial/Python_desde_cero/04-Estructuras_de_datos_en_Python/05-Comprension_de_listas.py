frutas = ["Manzana", "Platano", "Pera", "Mandarina", "Fresa", "Piña"]
copia_exacta = [fruta for fruta in frutas]
frutas_con_e = []

frutas_mayuscula = [fruta.upper() for fruta in frutas]
print(frutas_mayuscula)

# OPCIÓN 1
for fruta in frutas:
    if "e" in fruta:
        # Se agrega la fruta que contenga la letra e a la lista "frutas_con_e"
        frutas_con_e.append(fruta)

print(frutas_con_e)

# OPCIÓN 2
frutas_con_e_2 = [fruta for fruta in frutas if "e" in fruta]
print(frutas_con_e_2)

frutas_2 = [fruta if fruta != "Pera" else "Aguacate" for fruta in frutas]
print(frutas_2)
