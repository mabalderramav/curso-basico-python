dolares = input("Cuantos pesos bolivianos tienes?: ")
dolares = float(dolares)
tipo_cambio = 6.96
pesos_bolivianos = dolares * tipo_cambio
pesos_bolivianos = round(pesos_bolivianos, 2)
pesos_bolivianos = str(pesos_bolivianos)
print("tienes $" + pesos_bolivianos + " dolares")
