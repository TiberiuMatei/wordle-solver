import time
from typing import OrderedDict

from playwright.sync_api import sync_playwright

from starting_data.get_list_of_possible_words import GetListOfPossibleWords
from starting_data.get_possible_words_info import GetPossibleWordsInfo
from starting_data.get_starting_word import GetStartingWord
from wordle_guessing import WordleGuess
from wordle_selectors.wordle_selectors import WordleSelectors

TXT_FILE = "possible_words.txt"

def keep_guessing(page : object, guessed_word_data : list) -> None:
    """
    Logic for iterating through wordle guesses until the solution is found

    Args:
        page: Playwright browser page needed for web interaction
        guessed_word_data: The data needed for entering the next best guess (currently guessed word + the list of possible words)
    """
    solution_is_found = False
    
    while (solution_is_found is False):
        for attempt in range(2,7): # Iterate through next wordle guesses after the starting word is provided (rows 2 - 6 from game board)
            guess_scheme_data = OrderedDict() # Data scheme for entered guess needed for the next guess
            all_letters_state = [] # List of every letter state (absent | present | correct)
            letter_index = 0

            # Typing guessed word
            page.type(WordleSelectors.BOARD[f'WORD_{attempt}'], guessed_word_data[0])
            page.press(WordleSelectors.BOARD[f'WORD_{attempt}'], 'Enter')

            # Getting data for guessed word {index : [letter, letter_state]}
            for selector in WordleSelectors.BOARD_DATA[f'WORD_{attempt}'].values():
                time.sleep(0.5)
                guess_scheme_data[letter_index] = [page.inner_text(selector).lower(), page.get_attribute(selector, "data-state")] # {0: ['a', 'correct']}
                letter_index += 1

            # Getting the state for every letter (absent | present | correct)
            for letter_data in guess_scheme_data.values():
                all_letters_state.append(letter_data[1])
            
            # Checking if all the letters are 'correct'
            if len(set(all_letters_state)) == 1:
                solution_is_found = True
                break
            else:
                guessed_word_data = WordleGuess.guess_word(guess_scheme_data, guessed_word_data[1]) # keep filtering for the next guess
        break


# Getting initial list of words, words data and starting word
list_all_possbile_words = GetListOfPossibleWords.list_of_possible_words(TXT_FILE)
possible_words_data = GetPossibleWordsInfo.get_words_data(list_all_possbile_words)
starting_word = GetStartingWord.get_starting_word(possible_words_data)


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://www.nytimes.com/games/wordle/index.html")

    # Closing the cookies and the game info modals
    page.locator(WordleSelectors.CLOSE_COOKIES_RIBBON_BUTTON).click()
    page.locator(WordleSelectors.CLOSE_GAME_INFO_MODAL_BUTTON).click()

    # Data needed for letter info after using starting word
    guess_scheme_data = OrderedDict()
    letter_index = 0

    # Typing starting word
    page.type(WordleSelectors.BOARD['WORD_1'], starting_word)
    page.press(WordleSelectors.BOARD['WORD_1'], 'Enter')

    # Getting data for starting word {index : [letter, letter_state]}
    for letter, selector in WordleSelectors.BOARD_DATA['WORD_1'].items():
        time.sleep(0.5)
        guess_scheme_data[letter_index] = [page.inner_text(selector).lower(), page.get_attribute(selector, "data-state")] # {0: ['a', 'correct']}
        letter_index += 1
    
    # Using data from previous guess in order to take the next guess
    guessed_word_data = WordleGuess.guess_word(guess_scheme_data, list_all_possbile_words)

    keep_guessing(page, guessed_word_data)

    browser.close()
