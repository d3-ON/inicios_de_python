def divisors(num):
    try:
        if num < 0:
            raise ValueError('The number most be greater than 0')
        divisor = [i for i in range(1, num + 1) if num % i == 0]
        return divisor
    except ValueError as ve:
        print(ve)
       return False

def run():
        try: 
            num = int(input("Enter a number: "))
            print(divisors(num))
            print('Finished  the program')
        except ValueError:
            print('You must enter a number')

if __name__ == '__main__':
    run()
