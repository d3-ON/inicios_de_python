from data_filtering_db import DATA


def run():
# List comprehensions version:
    # all_python_devs = [worker['name'] for worker in DATA if worker['language'] == 'python']
# High order funtion version:
    # all_python_devs = list(map(lambda worker: worker['name'],
    #                         (list(filter(lambda worker: worker['language'] == 'python', DATA))))
    # )

# List comprehensions version:
    # all_Platzi_workers = [worker['name'] for worker in DATA if worker['organization'] == 'Platzi']
# High order funtion version:
    # all_Platzi_workers = list(map(lambda worker: worker['name'],
    #                             list(filter(lambda worker: worker['organization'] == 'Platzi', DATA)))
    # )


# High order funtion version:
    # adults = list(filter(lambda worker: worker['age']>=18, DATA))
    # adults = list(map(lambda worker: worker['name'], adults))
# List comprehensions version:
    # adults = [worker['name'] for worker in DATA if worker['age']>=18]

# High order funtion version:
    # old_people = list(map(lambda worker: worker | {'old': worker['age']>70}, DATA))
    # old_people = list(map(lambda worker: {**worker, **{"old": worker["age"] > 70}}, DATA)) #Versión alternativa para 3.5 < python < 3.9
# List comprehensions version:
    old_people = [worker | {'old': worker['age']>70}  for worker in DATA]


    for worker in old_people:
        print(worker)


if __name__ == '__main__':
    run()
