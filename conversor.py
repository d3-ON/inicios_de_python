dolar = float(input("Cuántos Dólares tienes? "))
valor_guarani = 0.00014
guarani = str(round(dolar / valor_guarani, 2))
print("Tienes " + guarani + " guaranies")
