class WordleSelectors:
    TERMS_CONTINUE = '//button[contains(text(),"Continue")]'
    CLOSE_COOKIES_RIBBON_BUTTON = '#pz-gdpr-btn-closex'
    CLOSE_GAME_INFO_MODAL_BUTTON = '//button[@class="Modal-module_closeIcon__TcEKb"]'
    PLAY_BUTTON = '//button[@data-testid="Play"]'
    BOARD = {
        'WORD_1': '//div[@aria-label="Row 1"]',
        'WORD_2': '//div[@aria-label="Row 2"]',
        'WORD_3': '//div[@aria-label="Row 3"]',
        'WORD_4': '//div[@aria-label="Row 4"]',
        'WORD_5': '//div[@aria-label="Row 5"]',
        'WORD_6': '//div[@aria-label="Row 6"]',
    }
    BOARD_DATA = {
        'WORD_1': {
            'LETTER_1': '//*[@id="wordle-app-game"]/div[1]/div/div[1]/div[1]/div',
            'LETTER_2': '//*[@id="wordle-app-game"]/div[1]/div/div[1]/div[2]/div',
            'LETTER_3': '//*[@id="wordle-app-game"]/div[1]/div/div[1]/div[3]/div',
            'LETTER_4': '//*[@id="wordle-app-game"]/div[1]/div/div[1]/div[4]/div',
            'LETTER_5': '//*[@id="wordle-app-game"]/div[1]/div/div[1]/div[5]/div',
        },
        'WORD_2': {
            'LETTER_1': '//*[@id="wordle-app-game"]/div[1]/div/div[2]/div[1]/div',
            'LETTER_2': '//*[@id="wordle-app-game"]/div[1]/div/div[2]/div[2]/div',
            'LETTER_3': '//*[@id="wordle-app-game"]/div[1]/div/div[2]/div[3]/div',
            'LETTER_4': '//*[@id="wordle-app-game"]/div[1]/div/div[2]/div[4]/div',
            'LETTER_5': '//*[@id="wordle-app-game"]/div[1]/div/div[2]/div[5]/div',
        },
        'WORD_3': {
            'LETTER_1': '//*[@id="wordle-app-game"]/div[1]/div/div[3]/div[1]/div',
            'LETTER_2': '//*[@id="wordle-app-game"]/div[1]/div/div[3]/div[2]/div',
            'LETTER_3': '//*[@id="wordle-app-game"]/div[1]/div/div[3]/div[3]/div',
            'LETTER_4': '//*[@id="wordle-app-game"]/div[1]/div/div[3]/div[4]/div',
            'LETTER_5': '//*[@id="wordle-app-game"]/div[1]/div/div[3]/div[5]/div',
        },
        'WORD_4': {
            'LETTER_1': '//*[@id="wordle-app-game"]/div[1]/div/div[4]/div[1]/div',
            'LETTER_2': '//*[@id="wordle-app-game"]/div[1]/div/div[4]/div[2]/div',
            'LETTER_3': '//*[@id="wordle-app-game"]/div[1]/div/div[4]/div[3]/div',
            'LETTER_4': '//*[@id="wordle-app-game"]/div[1]/div/div[4]/div[4]/div',
            'LETTER_5': '//*[@id="wordle-app-game"]/div[1]/div/div[4]/div[5]/div',
        },
        'WORD_5': {
            'LETTER_1': '//*[@id="wordle-app-game"]/div[1]/div/div[5]/div[1]/div',
            'LETTER_2': '//*[@id="wordle-app-game"]/div[1]/div/div[5]/div[2]/div',
            'LETTER_3': '//*[@id="wordle-app-game"]/div[1]/div/div[5]/div[3]/div',
            'LETTER_4': '//*[@id="wordle-app-game"]/div[1]/div/div[5]/div[4]/div',
            'LETTER_5': '//*[@id="wordle-app-game"]/div[1]/div/div[5]/div[5]/div',
        },
        'WORD_6': {
            'LETTER_1': '//*[@id="wordle-app-game"]/div[1]/div/div[6]/div[1]/div',
            'LETTER_2': '//*[@id="wordle-app-game"]/div[1]/div/div[6]/div[2]/div',
            'LETTER_3': '//*[@id="wordle-app-game"]/div[1]/div/div[6]/div[3]/div',
            'LETTER_4': '//*[@id="wordle-app-game"]/div[1]/div/div[6]/div[4]/div',
            'LETTER_5': '//*[@id="wordle-app-game"]/div[1]/div/div[6]/div[5]/div',
        },
    }
