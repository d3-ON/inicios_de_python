menu =int(input("""
Bienvenido al conversor de monedas 💴➡💱➡💵

1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos mexicanos

Elige una opción"""))

if menu ==1:
    pesos = float(input("Cuántos Pesos colombianos tienes? "))
    valor_dolar = 3870.40
    dolar = str(round(pesos / valor_dolar, 2))
    print("Tienes " + dolar + " dolares")
elif menu == 2:
    pesos = float(input("Cuántos Pesos argentinos tienes? "))
    valor_dolar = 97.30
    dolar = str(round(pesos / valor_dolar, 2))
    print("Tienes " + dolar + " dolares")
elif menu == 3:
    pesos = float(input("Cuántos Pesos mexicanos tienes? "))
    valor_dolar = 20.17
    dolar = str(round(pesos / valor_dolar, 2))
    print("Tienes " + dolar + " dolares")
else:
    print("Por favor ingresa una opción valida")
