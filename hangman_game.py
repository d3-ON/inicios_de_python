import random
import os   


def words_list():
    words_list = []
    
    with open('./Files/data.txt', 'r', encoding='utf-8') as f:
        for word in f:
            word = word.replace('\xad', '')
            words_list.append(word.strip())

    return words_list


def random_word(word):
    aleatory_word = random.choice(word)
    dict_word = {}
    counter = 0
    
    for i in aleatory_word:
        dict_word[counter] = i
        counter += 1   
        
    return dict_word

          

def run():
    step_1 = words_list()
    step_2 = random_word(step_1)
    


if __name__ == '__main__':
    run()