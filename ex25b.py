from ex25a import *

sentence = input("Gimme a sentence:\n>")

words = break_words(sentence)
print(words)
input('>')
sorted_words = sort_words(words)
print(sorted_words)
input('>')
print_first_word(words)
print_last_word(words)
input('>')
sorted_words = sort_sentence(sentence)
print_first_and_last(sentence)
input('>')
print_first_and_last_sorted(sentence)