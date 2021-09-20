def run():
    # Como 36 es multiplo de 4, 6 y 9 se coloca como multiplo para encontrar los numeros,
    #   envés de colocar i%4 == 0 and i%6 == 0 and i% 9 == 0
    # nums = [i for i in range(99999) if i%36 == 0]

    # if not controla si el valor es falso o vacio. Si no es falso i%36(diferente a 0),
    #   entonces es verdadero(igual a 0)
    nums = [i for i in range(1, 1000) if not i%36]

    print(nums)


if __name__ == '__main__':
    run()
