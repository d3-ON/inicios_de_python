import random

def bubble_sort(the_list):
    n = len(the_list)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            
            if the_list[j] > the_list[j + 1]:
                the_list[j], the_list[j + 1] = the_list[j + 1], the_list[j] 
 
    return the_list
 
 
if __name__ == '__main__':
    size_list = int(input('What size will the list be? '))

    the_list = [random.randint(0, 100) for i in range(size_list)]

    ordered_list = bubble_sort(the_list)
    
    print(ordered_list) 
