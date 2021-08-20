menu =int(input("""
Bienvenido al conversor de monedas 💴➡💱➡💵

1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos mexicanos

Elige una opción: """))

def conversor_monedas(pais, valor):
    pesos = float(input("Cuántos Pesos " + pais + " tienes?" ))
    valor_dolar = valor
    dolar = str(round(pesos / valor_dolar, 2))
    print("Tienes " + dolar + " dolares")

if menu == 1:
    conversor_monedas("colombianos", 3870.40)
elif menu == 2:
    conversor_monedas("argentinos", 97.29)
elif menu == 3:
    conversor_monedas("mexicanos", 20.15)
else:
    print("Por favor ingresa una opción valida")
