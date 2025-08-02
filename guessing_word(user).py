import random

choices = ["rainbow", "hello", "tree", "computer", "car"]

word = random.choice(choices)
chances = len(word)

print(f"It's a {len(word)} lettered word, you have {chances} chances.")
guess_word = ["_" for i in range(len(word))]

while chances > 0:
    guess = input("Guess a letter: ")
    if guess in word:
        print("Correct")
        for i in range(len(word)):
            if guess == word[i]:
                guess_word[i] = guess

    else:
        print("Incorrect")
        chances -= 1

    progress = "".join(guess_word)
    if progress == word:
        break
    print(progress)
    print(f"You have {chances} chances left.")

if "_" not in guess_word:
    print("You win!")
else:
    print("You lose!")

print(f'The word was "{word}"')

