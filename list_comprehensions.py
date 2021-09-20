def run():
    # natural_nums = []
    #
    # for i in range(101):
    #     num = i**2
    #     if num % 3 != 0:
    #         natural_nums.append(num)

    natural_nums = [i**2 for i in range(101) if i%3 != 0]

    print(natural_nums)


if __name__ == '__main__':
    run()
