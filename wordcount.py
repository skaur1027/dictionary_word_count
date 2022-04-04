"""Count words in file."""

import sys

def count_words(words):
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1 
    return word_count
    
def print_word_counts(word_count):
    for word, count in word_count.items():
        print(word, count)
        

def tokenize(filename):
    file = open(filename)
    
    word_count = {}
    for line in file:
        line = line.rstrip('\n')
        words = line.split(' ')
        word_count_line = count_words(words)
        for word, count in word_count_line.items():
            word_count[word] = word_count.get(word, 0) + count  
    print_word_counts(word_count)
    return tokenize

filename = sys.argv[1] 
tokenize(filename)
