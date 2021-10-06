import random
import os
from typing import Counter   
count = 0

def words_list():
    words_list = []
    
    with open('./Files/data.txt', 'r', encoding='utf-8') as f:
        for word in f:
            word = word.replace('\xad', '')
            words_list.append(word.strip())

    return words_list


def hidde_word(word):
    hidde = ''
    
    for i in range(len(word)):
        hidde += '_'
    
    return list(hidde)
              

def dict_word(word):
    dict_word = {}
    counter_ = 0
    
    for i in word:
        dict_word[counter_] = i
        counter_ += 1   
        
    return dict_word


def cleaner(word):
    word = (word.replace("'","").replace(',','')
            .replace('[','').replace(']',''))

    return word


def letter(dict, hidde, step_1):
    print(cleaner(str(hidde)))
    print(step_1)
    letter_entry = input('Type a lowercase letter and press enter: ')
    counter = 0
    global count

        
    for i, chars in enumerate(hidde):
            if letter_entry == dict.get(i):
                hidde[i] = dict[i]
                counter += 1
            # else:
            #     letter(dict, hidde, step_1)
    count += counter            
    # print('in' count)
    return hidde 


def run():
    step_1 = random.choice(words_list())
    step_2 = hidde_word(step_1)
    step_3 = dict_word(step_1)
    step_4 = step_2
    global count
    
    while count < len(step_1):
        step_4 = letter(step_3, step_4, step_1)
        # print('out' count)
                  
    print(cleaner(str(step_4)))          


if __name__ == '__main__':
    run()