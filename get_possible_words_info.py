class GetPossibleWordsInfo:
    @staticmethod
    def get_words_data(list_all_possbile_words : list) -> dict:
        """
        Get letter frequency for every word in the list of all possible words

        Args:
            list_all_possible_words (list) : list of all possible words

        Returns:
            Dictionary of counting letters for each word
            
            Example:
                {"aback" : {'a': 2, 'b': 1, 'c': 1, 'k': 1, 'unique_vowels_count': 1, 'unique_letters_count': 4}}
        """
        possible_words_data = {}
        vowels = set('aeiou')
        unique_vowels_count = 0

        for word in list_all_possbile_words:
            possible_words_data[word] = {} # adding the complete word as the key
            for letter in word:
                if letter in possible_words_data[word].keys():
                    possible_words_data[word][letter] += 1
                else:
                    possible_words_data[word][letter] = 1
                    if letter in vowels: # add the vowel count if first vowel occurence in word
                        unique_vowels_count += 1
            possible_words_data[word]["unique_vowels_count"] = unique_vowels_count
            possible_words_data[word]["unique_letters_count"] = len(possible_words_data[word].keys()) - 1 # subtract the unique_vowels_count key from unique letter count
            unique_vowels_count = 0 # reset unique vowel count for next word
        return possible_words_data
