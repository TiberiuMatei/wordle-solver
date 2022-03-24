from re import A
from statistics import correlation
from wordle_selectors import WordleSelectors

# absent | present | correct

class WordleGuess:
    @staticmethod
    def guess_word(guess_scheme_data : dict, list_all_possbile_words : list) -> str:
        filtered_possible_words = []
        absent_letters_in_word = set()
        present_letters_in_word = set()
        correct_letters_in_word = set()

        for letter,data in guess_scheme_data.items():
            match data[1]:
                case "absent":
                    absent_letters_in_word.add(letter)
                case "present":
                    present_letters_in_word.add(letter)
                case "correct":
                    correct_letters_in_word.add(letter)
        
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
        print("aaa")
