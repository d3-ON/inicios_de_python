def run():
    list = [1, 2, 3, 4, 5]
    # list_2 = []
    #
    # for i in list:
    #     list_2.append(i**2)

    list_2 = [i**2 for i in list]

    print(list_2)

if __name__ == '__main__':
    run()
