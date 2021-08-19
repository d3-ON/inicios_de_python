menu = """
Bienvenido al conversor de monedas 💴➡💱➡💵

1- Pesos colombianos
2- Pesos argentinos
3- Pesos mexicanos

Elige una opción"""

dolar = float(input("Cuántos Dólares tienes? "))
valor_guarani = 0.00014
guarani = str(round(dolar / valor_guarani, 2))
print("Tienes " + guarani + " guaranies")
