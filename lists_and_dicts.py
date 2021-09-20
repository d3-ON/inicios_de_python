def run():
    my_list = [1, 'hello', True, 4.5]
    my_dict = {'firstname': 'Diego', 'lastname': 'López'}

    super_list = [
        {'firstname': 'Diego', 'lastname': 'López'},
        {'firstname': 'Miguel', 'lastname': 'Torres'},
        {'firstname': 'Pepe', 'lastname': 'Rodelo'},
        {'firstname': 'Susana', 'lastname': 'Matinez'},
        {'firstname': 'José', 'lastname': 'Garcia'},
    ]

    super_dict = {
        'natural_nums': [1, 2, 3, 4, 5],
        'intger_nums': [-1, -2, 0, 1, 2],
        'floating_nums': [1.1, 4.5, 6.43]
    }

    for key, value in super_dict.items():
        print(f'{key} - {value}')

    for i in super_list:
        for key, value in i.items():
            print(f'{key} - {value}')

if __name__ == '__main__':
    run()
