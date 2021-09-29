import random
import os   


def words_list():
    words_list = []
    
    with open('./Files/data.txt', 'r', encoding='utf-8') as f:
        for word in f:
            word = word.replace('\xad', '')
            words_list.append(word.strip())

    return words_list


def hiden(word):
    hiden_word = ''
    
    for i in word:
        hiden_word += i.replace(i, '_ ')
    
    return hiden_word
    
    
# def letter():
#     letter_in = input('Enter a lowercase letter: ')
#     for i in :
          


def run():
    random_word = random.choice(words_list())
    
    print(hiden(random_word))
    


if __name__ == '__main__':
    run()