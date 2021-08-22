
# def run(res, num):
#     if res < 1000000:
#         res = 2 ** num
#         print(res)
#         run(res, num + 1)
# run(0, 0)

def run():
     LIMITE = 1000000

     contador = 0
     potencia_2 = 2 ** contador
     while potencia_2 < LIMITE:
         print("2 elevado a " + str(contador) + " es igual a: " + str(potencia_2))
         contador = contador + 1
         potencia_2 = 2 ** contador


if __name__ == "__main__":
    run()
