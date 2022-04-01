import random

from starting_data.get_possible_words_info import GetPossibleWordsInfo


class WordleGuess:
    @staticmethod
    def guess_word(guess_scheme_data : dict, list_all_possbile_words : list) -> list:
        """
        The logic for filtering words and returning a next best guess based on a previously entered word

        Args:
            guess_scheme_data: Dictionary containing the data for the currently guessed word (letter, letter position and letter state)
            list_all_possbile_words: List of possible words that contains the possible solution

        Returns:
            List containing the randomly guessed word and the filtered list of possible guesses
        """
        filtered_possible_words = [] # Resulting list of words after filtering

        absent_letters_in_word = set()

        present_letters_in_word = set()
        present_letters_data = {} # {0: ['a', 'correct']}

        correct_letters_in_word = set()
        correct_letters_data = {} # {0: ['a', 'correct']}

        # data = [letter, letter_state = absent | present | correct]
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
        if len(absent_letters_in_word) != 0:
            for word in list_all_possbile_words:
                absent_letter_flag = False
                for letter in word:
                    if letter in absent_letters_in_word and letter not in correct_letters_in_word and letter not in present_letters_in_word:
                        absent_letter_flag = True
                        break
                if not absent_letter_flag:
                    filtered_possible_words.append(word)

        # Filter out words that do NOT contain any of the 'correct' letters
        if len(correct_letters_in_word) != 0:
            if filtered_possible_words is not []: # if filtering was previously done based on the 'absent' letters
                words_data = GetPossibleWordsInfo.get_letter_index_from_words(filtered_possible_words) # example: words_data = {"weary" : {0: 'w', 1: 'e', 2: 'a', 3: 'r', 4: 'y'}}

                for index, correct_letter_data in correct_letters_data.items(): # {0: ['a', 'correct']}
                    for word, word_data in words_data.items(): # {"weary" : {0: 'w', 1: 'e', 2: 'a', 3: 'r', 4: 'y'}}
                        if word_data[index] != correct_letter_data[0]: # if the 'correct' letter is not present at the 'correct' index, remove the word
                            if word in filtered_possible_words:
                                filtered_possible_words.remove(word)
                            else:
                                continue
            else:
                filtered_possible_words = list_all_possbile_words.copy()
                words_data = GetPossibleWordsInfo.get_letter_index_from_words(filtered_possible_words) # example: words_data = {"weary" : {0: 'w', 1: 'e', 2: 'a', 3: 'r', 4: 'y'}}

                for index, correct_letter_data in correct_letters_data.items(): # {0: ['a', 'correct']}
                    for word, word_data in words_data.items(): # {"weary" : {0: 'w', 1: 'e', 2: 'a', 3: 'r', 4: 'y'}}
                        if word_data[index] != correct_letter_data[0]: # if the 'correct' letter is not present at the 'correct' index, remove the word
                            if word in filtered_possible_words:
                                filtered_possible_words.remove(word)
                            else:
                                continue

        # Filter and find words that cotain the 'present' letters at different indices
        if len(present_letters_in_word) != 0:
            if filtered_possible_words is not []: # if filtering was previously done based on the 'absent' letters
                words_data = GetPossibleWordsInfo.get_letter_index_from_words(filtered_possible_words) # example: words_data = {"weary" : {0: 'w', 1: 'e', 2: 'a', 3: 'r', 4: 'y'}}            
                for index, present_letter_data in present_letters_data.items(): # {0: ['a', 'present']}
                    for word, word_data in words_data.items(): # {"weary" : {0: 'w', 1: 'e', 2: 'a', 3: 'r', 4: 'y'}}
                        if present_letter_data[0] not in word:
                            if word in filtered_possible_words:
                                filtered_possible_words.remove(word)
                            else:
                                continue
                
                words_data = GetPossibleWordsInfo.get_letter_index_from_words(filtered_possible_words) # example: words_data = {"weary" : {0: 'w', 1: 'e', 2: 'a', 3: 'r', 4: 'y'}}  
                for index, present_letter_data in present_letters_data.items(): # {0: ['a', 'present']}
                    for word, word_data in words_data.items(): # {"weary" : {0: 'w', 1: 'e', 2: 'a', 3: 'r', 4: 'y'}}
                        if word_data[index] == present_letter_data[0]: # if the 'present' letter is present at the 'present' index, remove the word
                            if word in filtered_possible_words:
                                filtered_possible_words.remove(word)
                            else:
                                continue
            else:
                filtered_possible_words = list_all_possbile_words.copy()
                words_data = GetPossibleWordsInfo.get_letter_index_from_words(filtered_possible_words) # example: words_data = {"weary" : {0: 'w', 1: 'e', 2: 'a', 3: 'r', 4: 'y'}}
                for index, present_letter_data in present_letters_data.items(): # {0: ['a', 'present']}
                    for word, word_data in words_data.items(): # {"weary" : {0: 'w', 1: 'e', 2: 'a', 3: 'r', 4: 'y'}}
                        if present_letter_data[0] not in word:
                            if word in filtered_possible_words:
                                filtered_possible_words.remove(word)
                            else:
                                continue
                
                words_data = GetPossibleWordsInfo.get_letter_index_from_words(filtered_possible_words) # example: words_data = {"weary" : {0: 'w', 1: 'e', 2: 'a', 3: 'r', 4: 'y'}}
                for index, present_letter_data in present_letters_data.items(): # {0: ['a', 'correct']}
                    for word, word_data in words_data.items(): # {"weary" : {0: 'w', 1: 'e', 2: 'a', 3: 'r', 4: 'y'}}
                        if word_data[index] == present_letter_data[0]: # if the 'present' letter is present at the 'present' index, remove the word
                            if word in filtered_possible_words:
                                filtered_possible_words.remove(word)
                            else:
                                continue
        if filtered_possible_words == []: # If the word is not present in the possible_words.txt
            return ["N/A", "N/A"]
        else:
            return [random.choice(filtered_possible_words), filtered_possible_words]
