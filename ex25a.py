def break_words(stuff):
    """this will break up words for us"""
    return stuff.split(' ') # split string into a list

def sort_words(words):
    return sorted(words)

def print_first_word(words):
    print(words.pop(0)) # 0 je na početku liste

def print_last_word(words):
    print(words.pop(-1)) #-1 je za kraj liste

def sort_sentence(sentence):
    return sort_words(break_words(sentence))

def print_first_and_last(sentence):
    print_first_word(break_words(sentence))
    print_last_word(break_words(sentence))

def print_first_and_last_sorted(sentence):
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)



