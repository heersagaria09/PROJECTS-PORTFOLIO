import random

words = ["python", "hangman", "coding", "program", "developer"]
chosen_word = random.choice(words)
display = ["_"] * len(chosen_word)
lives = 6
guessed_letters = []

print("Welcome to Hangman! You have 6 lives. Good luck!")

while lives > 0 and "_" in display:
    print("\nWord:", " ".join(display))
    print("Guessed:", ", ".join(guessed_letters) if guessed_letters else "None")
    print("Lives left:", lives)
    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter (a–z).")
        continue
    if guess in guessed_letters:
        print("You've already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in chosen_word:
        for i, ch in enumerate(chosen_word):
            if ch == guess:
                display[i] = guess
        print("Nice! That letter is in the word.")
    else:
        lives -= 1
        print("Oops! That letter is not in the word.")

if "_" not in display:
    print("\n🎉 You won! The word was:", chosen_word)
else:
    print("\n💀 You lost. The word was:", chosen_word)