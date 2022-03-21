class GetListOfPossibleWords:
    @staticmethod
    def list_of_possible_words(txt_file : str) -> list:
        """
        Returning a list of possible 5 letter words from a txt file

        Args:
            txt_file: String with the complete .txt name of the txt file from within the project

        Returns:
            List containing ~2499 5 letter words that are possible guesses
        """
        with open(txt_file, 'r') as txt_file:
            return txt_file.read().splitlines()