pesos_bolivianos = input("Cuantos pesos bolivianos tienes?: ")
pesos_bolivianos = float(pesos_bolivianos)
valor_dolar = 6.96
dolares = pesos_bolivianos / valor_dolar
dolares = round(dolares, 2)
dolares = str(dolares)
print("tienes $" + dolares + " dolares")
