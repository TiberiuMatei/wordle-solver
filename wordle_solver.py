import time
from typing import OrderedDict

from get_list_of_possible_words import GetListOfPossibleWords
from get_possible_words_info import GetPossibleWordsInfo
from get_starting_word import GetStartingWord
from wordle_guessing import WordleGuess
from wordle_selectors import WordleSelectors
from playwright.sync_api import sync_playwright

TXT_FILE = "possible_words.txt"
word_of_the_day = "level"

# https://www.wordleunlimited.com/

list_all_possbile_words = GetListOfPossibleWords.list_of_possible_words(TXT_FILE)

possible_words_data = GetPossibleWordsInfo.get_words_data(list_all_possbile_words)
starting_word = GetStartingWord.get_starting_word(possible_words_data)

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.nytimes.com/games/wordle/index.html")
    page.locator(WordleSelectors.CLOSE_COOKIES_RIBBON_BUTTON).click()
    page.locator(WordleSelectors.CLOSE_GAME_INFO_MODAL_BUTTON).click()

    page.type(WordleSelectors.BOARD['WORD_1'], starting_word)
    page.press(WordleSelectors.BOARD['WORD_1'], 'Enter')

    guess_scheme_data = OrderedDict()
    position = 0

    for letter, selector in WordleSelectors.BOARD_DATA['WORD_1'].items():
        time.sleep(0.5)
        guess_scheme_data[position] = [page.inner_text(selector).lower(), page.get_attribute(selector, "data-state")]
        position += 1
    
    WordleGuess.guess_word(guess_scheme_data, list_all_possbile_words)

    browser.close()
