class WordleSelectors:
    CLOSE_COOKIES_RIBBON_BUTTON = '#pz-gdpr-btn-closex'
    CLOSE_GAME_INFO_MODAL_BUTTON = 'game-modal path'
    BOARD = {
        'WORD_1' : 'game-row:nth-child(1) .row',
        'WORD_2' : 'game-row:nth-child(2) .row',
        'WORD_3' : 'game-row:nth-child(3) .row',
        'WORD_4' : 'game-row:nth-child(4) .row',
        'WORD_5' : 'game-row:nth-child(5) .row',
        'WORD_6' : 'game-row:nth-child(6) .row',
    }
    BOARD_DATA = {
        'WORD_1' : {
            'LETTER_1' : 'game-row:nth-child(1) .row game-tile:nth-child(1) .tile',
            'LETTER_2' : 'game-row:nth-child(1) .row game-tile:nth-child(2) .tile',
            'LETTER_3' : 'game-row:nth-child(1) .row game-tile:nth-child(3) .tile',
            'LETTER_4' : 'game-row:nth-child(1) .row game-tile:nth-child(4) .tile',
            'LETTER_5' : 'game-row:nth-child(1) .row game-tile:nth-child(5) .tile',
        },
        'WORD_2' : {
            'LETTER_1' : 'game-row:nth-child(2) .row game-tile:nth-child(1) .tile',
            'LETTER_2' : 'game-row:nth-child(2) .row game-tile:nth-child(2) .tile',
            'LETTER_3' : 'game-row:nth-child(2) .row game-tile:nth-child(3) .tile',
            'LETTER_4' : 'game-row:nth-child(2) .row game-tile:nth-child(4) .tile',
            'LETTER_5' : 'game-row:nth-child(2) .row game-tile:nth-child(5) .tile',
        },
        'WORD_3' : {
            'LETTER_1' : 'game-row:nth-child(3) .row game-tile:nth-child(1) .tile',
            'LETTER_2' : 'game-row:nth-child(3) .row game-tile:nth-child(2) .tile',
            'LETTER_3' : 'game-row:nth-child(3) .row game-tile:nth-child(3) .tile',
            'LETTER_4' : 'game-row:nth-child(3) .row game-tile:nth-child(4) .tile',
            'LETTER_5' : 'game-row:nth-child(3) .row game-tile:nth-child(5) .tile',
        },
        'WORD_4' : {
            'LETTER_1' : 'game-row:nth-child(4) .row game-tile:nth-child(1) .tile',
            'LETTER_2' : 'game-row:nth-child(4) .row game-tile:nth-child(2) .tile',
            'LETTER_3' : 'game-row:nth-child(4) .row game-tile:nth-child(3) .tile',
            'LETTER_4' : 'game-row:nth-child(4) .row game-tile:nth-child(4) .tile',
            'LETTER_5' : 'game-row:nth-child(4) .row game-tile:nth-child(5) .tile',
        },
        'WORD_5' : {
            'LETTER_1' : 'game-row:nth-child(5) .row game-tile:nth-child(1) .tile',
            'LETTER_2' : 'game-row:nth-child(5) .row game-tile:nth-child(2) .tile',
            'LETTER_3' : 'game-row:nth-child(5) .row game-tile:nth-child(3) .tile',
            'LETTER_4' : 'game-row:nth-child(5) .row game-tile:nth-child(4) .tile',
            'LETTER_5' : 'game-row:nth-child(5) .row game-tile:nth-child(5) .tile',
        },
        'WORD_6' : {
            'LETTER_1' : 'game-row:nth-child(6) .row game-tile:nth-child(1) .tile',
            'LETTER_2' : 'game-row:nth-child(6) .row game-tile:nth-child(2) .tile',
            'LETTER_3' : 'game-row:nth-child(6) .row game-tile:nth-child(3) .tile',
            'LETTER_4' : 'game-row:nth-child(6) .row game-tile:nth-child(4) .tile',
            'LETTER_5' : 'game-row:nth-child(6) .row game-tile:nth-child(5) .tile',
        },
    }
