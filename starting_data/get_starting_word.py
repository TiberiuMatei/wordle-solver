import random


class GetStartingWord:
    @staticmethod
    def get_starting_word(possible_words_data : dict) -> str:
        """
        Gets a random starting word based on number of unique vowels and unique overall letters

        Args:
            possible_words_data (dict) : data for each possible word including letter frequency, unique vowel count and unique letter count

        Returns:
            Random string that will be used as starting word
        """
        starting_words = []
        for word, data in possible_words_data.items():
            if data["unique_letters_count"] == 5 and data["unique_vowels_count"] >= 2: # starting word should have all the letters unique
                starting_words.append(word)
        return random.choice(starting_words)
