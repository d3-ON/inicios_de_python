from hangman_drawing import PICS
import random
import os

count = 0
attemps = 0
entry = False
saved_letter = False

letter_already = []
DATA = ['a', 'á', 'b', 'c', 'd', 'e', 'é', 'f', 'g', 'h', 'i', 'í', 
        'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'ó', 'p', 'q', 
        'r', 's', 't', 'u', 'ú', 'v', 'w', 'x', 'y', 'z']
ACCENT = {'á':'a', 'é':'e', 'í':'i', 'ó':'o', 'ú':'u'}


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
        # if i == 2:
        #     hidde += ' '
        # else: 
            # hidde += '_'

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


def mechanics(letter, dict, hidde):
    # print(cleaner(str(hidde)))
    # print(step_1)
    # letter_entry = input('Type a lowercase letter and press enter: ')
    global entry
    global ACCENT
    global DATA 
    global letter_already
    global saved_letter
    
    for j in DATA:
        if letter == j:    
            for i, chars in enumerate(hidde):
                        if letter == dict[i]:
                            hidde[i] = dict[i]
                            entry = True
                            saved_letter = True 
                            for key, value in ACCENT.items():
                                if dict[i] == key and letter == value:
                                    hidde[i] = key
                                    entry = True
                                    saved_latter = False
                        else:
                            for k in letter_already:
                                if k == letter:
                                    entry = False
    return hidde 


def run():
    step_1 = 'colegio' #random.choice(words_list())
    step_2 = hidde_word(step_1)
    step_3 = dict_word(step_1)
    step_4 = step_2
    global letter_already
    global count
    global attemps
    global entry
    global saved_letter
            
    while count < len(step_1):
        os.system('cls')
        print(cleaner(str(step_2)))
        print(step_1)
        print(PICS[attemps])
        letter_in = input('Type a lowercase letter and press enter: ')
            
        step_4 = mechanics(letter_in,step_3, step_4)
        if entry:
            count += 1            
        elif not entry:
            attemps += 1
        entry = False
        # os.system('cls')
        if saved_letter:
            letter_already.append(letter_in)
        saved_letter = False
            
        print(letter_already)
                          
    print(cleaner(str(step_4)))
    if attemps == 6:
        print('You lose')          


if __name__ == '__main__':
    run()