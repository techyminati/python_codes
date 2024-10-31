import random

def choose_word():
    words = ["python", "hangman", "programming", "developer", "challenge"]
    return random.choice(words)

def display_hangman(attempts):
    stages = [
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / \\
           |
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   /
           |
        """,
        """
           ------
           |    |
           |    O
           |   /|
           |   
           |
        """,
        """
           ------
           |    |
           |    O
           |    
           |   
           |
        """,
        """
           ------
           |    |
           |    
           |    
           |   
           |
        """,
        """
           ------
           |    
           |    
           |    
           |   
           |
        """,
        """
           ------
           |    
           |    
           |    
           |   
           |
        """
    ]
    return stages[attempts]

def hangman():
    word = choose_word()
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    attempts = 6

    print("Welcome to Hangman!")
    print(display_hangman(attempts))
    print("Word to guess:", " ".join(word_completion))

    while not guessed and attempts > 0:
        guess = input("Please enter a letter or word: ").lower()

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed that letter:", guess)
            elif guess not in word:
                print("Wrong guess:", guess)
                attempts -= 1
                guessed_letters.append(guess)
            else:
                print("Good guess:", guess)
                guessed_letters.append(guess)
                word_completion = "".join([letter if letter in guessed_letters else "_" for letter in word])

                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed that word:", guess)
            elif guess != word:
                print("Wrong guess:", guess)
                attempts -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Invalid input. Please try again.")

        print(display_hangman(attempts))
        print("Word to guess:", " ".join(word_completion))

    if guessed:
        print("Congratulations! You've guessed the word:", word)
    else:
        print("Sorry, you ran out of attempts. The word was:", word)

if __name__ == "__main__":
    hangman()
