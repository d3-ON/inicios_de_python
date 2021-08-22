def run():
    # for contador in range(1000):
    #     if contador % 2 != 0:
    #         continue
    #     print(contador)

    # for i in range(0, 10000):
    #     print(i)
    #     if i  == 5678:
    #         break

    # texto = input("Escribe un texto: ")
    # for letra in texto:
    #     if letra == "o":
    #         break
    #     print(letra)

# ////////////////////////////////////////////////////////////////////////

    # contador = 0
    # while contador < 1000:
    #     contador += 1
    #     if contador % 2 != 0:
    #         continue
    #     print(contador)

    # i = 0
    # while i < 10000:
    #     print(i)
    #     i += 1
    #     if i ==  5678:
    #         break

    texto = input("Escribe un texto: ")
    letra = None
    i = 0
    while letra != texto:
        letra = texto[i]
        if letra == "o":
            break
        print(letra)
        i += 1


if __name__ == "__main__":
    run()
