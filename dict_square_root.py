from math import sqrt


def run():
    # classic
    # dict = {i: i**0.5 for i in range(1001)}

    # math method
    dict = {i: sqrt(i) for i in range(1001)}

    print(dict)


if __name__ == '__main__':
    run()
