 ![wordle-logo](/ui/assets/readme-cover.png)
 
 ## Description
 
 ***wordle-solver*** aims to find the solution for the [Wordle](https://www.nytimes.com/games/wordle/index.html) game in as few guesses as possible by progressively filtering out words. It features a light user interface from which the user can start and read the solution data (solution and the number of needed guesses). The program works by having an existing list of possible words, starting with a best possible word (a 5-letter word that has no duplicate letters and at least 2 vowels) and programatically filtering out words based on the entered word data.
 
 ## Installation
 
Prerequisites: pip, venv (use of virtual environment strongly recommended)
 
1. After cloning the project, select the project directory and create a venv: ```python -m venv wordle-solver-venv```
2. After the venv is created, access the venv and activate it: ```cd wordle-solver-venv\Scripts``` and ```activate```
3. After the venv is active, return to the root of the cloned project: ```cd ..\..```
4. Install the project requirements: ```pip install -r requirements.txt```


The list of needed libraries: [requirements.txt](/requirements.txt)

5. Wait for the libraries to install
6. Run the wordle-solver by using: ```python wordle_solver.py```

***NOTE:*** Check that the screen scaling is set to 100% for the correct display of the application.

## Usage

1. Click on the ***ENTER*** button ![app-main-window](/ui/assets/app-main-window.png)
2. A Chromium browser page will open and the solver will start guessing and inputting directly in the browser page
3. When the solution is found, the browser will close, and the application main window will display the solution as well as the needed guesses ![app-solution](/ui/assets/app-solution.png)

## Notes

- If the program doesn't succeed in finding the solution, it will display ***N/A 0/6***. Possible causes:
  - the solution was not efficiently selected, try running again
  - the word is not present in the [possible_words.txt](/possible_words.txt). Manually add the word and try running again
