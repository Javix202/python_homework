def make_hangman(secret_word):
    guesses = []

    def hangman_closure(letter):
        guesses.append(letter)
        display = ""
        for ch in secret_word:
            display += ch if ch in guesses else "_"
        print(display)
        return all(ch in guesses for ch in secret_word)

    return hangman_closure

secret = input("Secret word: ")
game = make_hangman(secret)

while True:
    guess = input("Guess a letter: ")
    if game(guess):
        print("You guessed the word!")
        break