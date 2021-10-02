import random
import os   


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
    counter = 0
    
    for i in word:
        dict_word[counter] = i
        counter += 1   
        
    return dict_word

def letter_in():
    letter = input('')


def character_cleaner(word):
    word = (word.replace("'","").replace(',','')
            .replace('[','').replace(']',''))
    
    # clean = ''
    # for i in word:
    #     if i != '_' and i != ' ' and i != "letra que ingresa el usuario":
    #         i = i.replace(i, '')
    #     clean += i

    return word


def run():
    step_1 = random.choice(words_list())
    step_2 = str(hidde_word(step_1))
    step_3 = dict_word(step_1)
    
    print(character_cleaner(step_2))
    print(step_3)

if __name__ == '__main__':
    run()