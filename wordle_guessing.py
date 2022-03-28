from get_possible_words_info import GetPossibleWordsInfo
from wordle_selectors import WordleSelectors

# letter_state = absent | present | correct
# *_letters_data = {0: ['a', 'correct']}
# words_data = {"weary" : {0: 'w', 1: 'e', 2: 'a', 3: 'r', 4: 'y'}}

class WordleGuess:
    @staticmethod
    def guess_word(guess_scheme_data : dict, list_all_possbile_words : list) -> str:
        filtered_possible_words = []

        absent_letters_in_word = set()

        present_letters_in_word = set()
        present_letters_data = {}

        correct_letters_in_word = set()
        correct_letters_data = {}

        # data = [letter, letter_state]
        for index,data in guess_scheme_data.items():
            match data[1]:
                case "absent":
                    absent_letters_in_word.add(data[0])
                case "present":
                    present_letters_in_word.add(data[0])
                    present_letters_data[index] = data
                case "correct":
                    correct_letters_in_word.add(data[0])
                    correct_letters_data[index] = data
        
        # Filter out words that contain any 'absent' letters from the previous word        
        if absent_letters_in_word is not set():
            for word in list_all_possbile_words:
                absent_letter_flag = False
                for letter in word:
                    if letter in absent_letters_in_word:
                        absent_letter_flag = True
                        break
                if not absent_letter_flag:
                    filtered_possible_words.append(word)

        if correct_letters_in_word is not set():
            if filtered_possible_words is not []:
                words_data = GetPossibleWordsInfo.get_letter_index_from_words(filtered_possible_words)

                for index, correct_letter_data in correct_letters_data.items():
                    for word, word_data in words_data.items():
                        if word_data[index] != correct_letter_data[0]:
                            if word in filtered_possible_words:
                                filtered_possible_words.remove(word)
                            else:
                                continue

            else:
                words_data = GetPossibleWordsInfo.get_letter_index_from_words(list_all_possbile_words)

                for index, correct_letter_data in correct_letters_data.items():
                    for word, word_data in words_data.items():
                        if word_data[index] is not correct_letter_data[0]:
                            filtered_possible_words.remove(word)
            

        print("aaa")
