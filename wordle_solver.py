import os
import sys
import time
from typing import OrderedDict

from playwright.sync_api import sync_playwright
from PySide6 import QtCore, QtGui
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor
from PySide6.QtWidgets import *

import ui.wordle_solver_qrc
from starting_data.get_list_of_possible_words import GetListOfPossibleWords
from starting_data.get_possible_words_info import GetPossibleWordsInfo
from starting_data.get_starting_word import GetStartingWord
from wordle_guessing import WordleGuess
from wordle_selectors.wordle_selectors import WordleSelectors

os.system('pyside6-rcc ui/wordle_solver_qrc.qrc -o ui/wordle_solver_qrc.py')

from ui.ui_wordle_window import \
    Ui_ui_wordle_solver_main_window  # UI File for main window

TXT_FILE = "possible_words.txt"

def keep_guessing(page : object, guessed_word_data : list) -> list:
    """
    Logic for iterating through wordle guesses until the solution is found

    Args:
        page: Playwright browser page needed for web interaction
        guessed_word_data: The data needed for entering the next best guess (currently guessed word + the list of possible words)
    
    Returns:
        List containing the solution and the attempt number eg ['crane', 2]
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
            
            # Checking if all the letters are 'correct' and if the solution is found
            # If the solution is not found return N/A 0/6
            if set(all_letters_state) == {'correct'}:
                solution_is_found = True
                return [guessed_word_data[0], attempt]
            elif attempt == 6:
                return ["N/A", 0]
            else:
                guessed_word_data = WordleGuess.guess_word(guess_scheme_data, guessed_word_data[1]) # keep filtering for the next guess
        break


def solve_wordle() -> list:
    """
    Logic for solving wordle
    
    Returns:
        List containing the solution and the attempt number: eg ['crane', 2]
    """

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
        all_letters_state = []

        # Typing starting word
        page.type(WordleSelectors.BOARD['WORD_1'], starting_word)
        page.press(WordleSelectors.BOARD['WORD_1'], 'Enter')

        # Getting data for starting word {index : [letter, letter_state]}
        for selector in WordleSelectors.BOARD_DATA['WORD_1'].values():
            time.sleep(0.5)
            guess_scheme_data[letter_index] = [page.inner_text(selector).lower(), page.get_attribute(selector, "data-state")] # {0: ['a', 'correct']}
            letter_index += 1

        # Getting the state for every letter (absent | present | correct)
        for letter_data in guess_scheme_data.values():
            all_letters_state.append(letter_data[1])
        
        # Checking if all the letters are 'correct' and the starting word was the solution
        if set(all_letters_state) == {'correct'}:
            return [starting_word, 1]
        else:
            # Using data from previous guess in order to take the next guess
            guessed_word_data = WordleGuess.guess_word(guess_scheme_data, list_all_possbile_words)
            return keep_guessing(page, guessed_word_data)


class UiWordleSolver(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_ui_wordle_solver_main_window()
        self.ui.setupUi(self)

        # REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # SET DROPSHADOW WINDOW
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 100))

        # Move window
        def moveWindow(event):
            # If left click hold - move window
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPosition().toPoint() - self.dragPos)
                self.dragPos = event.globalPosition().toPoint()
                event.accept()

        # Set title bar
        self.ui.ui_top_bar.mouseMoveEvent = moveWindow

        # APPLY DROPSHADOW TO FRAME
        self.ui.ui_main_window.setGraphicsEffect(self.shadow)

        # MINIMIZE
        self.ui.ui_minimize_button.clicked.connect(lambda: self.showMinimized())
        self.ui.ui_minimize_button.setToolTip("Minimize")

        # CLOSE
        self.ui.ui_close_button.clicked.connect(lambda: self.close())
        self.ui.ui_close_button.setToolTip("Close")

        # Set title name
        self.setWindowTitle("Wordle Solver")

        # Set window icon
        self.setWindowIcon(QtGui.QIcon(":/assets/assets/ui-logo.png"))

        # Solve Wordle from ENTER button
        self.ui.ui_enter_button.clicked.connect(self.solve_wordle_from_ui)

        # Show Main Window
        self.show()
    
    # Move app window - drag
    def mousePressEvent(self, event):
        self.dragPos = event.globalPosition().toPoint()
    
    def solve_wordle_from_ui(self):
        results_to_display = solve_wordle()
        self.ui.ui_result_word_label.setText("  ".join(results_to_display[0].upper()))
        self.ui.ui_result_attempt_label.setText(f"{results_to_display[1]} / 6")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = UiWordleSolver()
    sys.exit(app.exec())
