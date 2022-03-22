from get_list_of_possible_words import GetListOfPossibleWords
from get_possible_words_info import GetPossibleWordsInfo
from get_starting_word import GetStartingWord

TXT_FILE = "possible_words.txt"

# https://www.wordleunlimited.com/

list_all_possbile_words = GetListOfPossibleWords.list_of_possible_words(TXT_FILE)
possible_words_data = GetPossibleWordsInfo.get_words_data(list_all_possbile_words)
starting_word = GetStartingWord.get_starting_word(possible_words_data)

print("aaaa")