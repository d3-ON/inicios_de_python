import random
import os
count = 0
accent = {'á':'a', 'é':'e', 'í':'i', 'ó':'o', 'ú':'u'}

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
        if i == 2:
            hidde += ' '
        else: 
            hidde += '_'

    return list(hidde)
              

def dict_word(word):
    counter = 0
    
    dict_word = {}
    
    for i in word:
        dict_word[counter] = i
        counter += 1   
        
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
    global accent
        
    for i, chars in enumerate(hidde):
        # for j in DATA:
        #     if letter_entry == j:
        if letter_entry == dict.get(i):
            hidde[i] = dict[i]
            counter += 1                
        else:
            for key, value in accent.items():
                if dict.get(i) == key and letter_entry == value:
                    hidde[i] = key
                    counter += 1
            # elif letter_entry != j:
                
            #     letter(dict, hidde, step_1)
    count += counter            

    return hidde 


def run():
    step_1 = 'te amo'#random.choice(words_list())
    step_2 = hidde_word(step_1)
    step_3 = dict_word(step_1)
    step_4 = step_2
    global count
    
    while count < len(step_1):
        os.system('cls')
        step_4 = letter(step_3, step_4, step_1)
        # print('out' count)
        os.system('cls')

                  
    print(cleaner(str(step_4)))          


if __name__ == '__main__':
    run()