#  Command-Line Hangman Game

A classic, interactive **Hangman Game** built completely from scratch using Python.

The program randomly selects a word from a list, dynamically determines the number of allowed attempts based on the word's unique characters, tracks player input, and loops seamlessly so you can play multiple rounds without restarting the script.

#  Features
- **Dynamic Attempt Scaling:** Calculates the number of attempts fairly based on how many unique characters are in the secret word.
- **Input Handling:** Converts all user guesses to lowercase to ensure the game logic is case-insensitive.
- **Interactive Game Loop:** Built with a primary menu structure that allows players to seamlessly start new games or quit when finished.
- **Structured Architecture:** Keeps code clean and modular by dividing the layout into clear `hangman()` and `main()` execution blocks.

#  Core Concepts Practiced
Building this project was an excellent way to apply fundamental programming patterns:
- Control flow structures (while loops, if/else statements).
- Data Collections (using lists to track matched strings and sets to extract unique letters).
- Code modularity (utilizing conditional block controls like if __name__ == "__main__":).
