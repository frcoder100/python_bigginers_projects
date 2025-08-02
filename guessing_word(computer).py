import random
import string

letters = list(string.ascii_lowercase)

print("Choose a word")
length = int(input("How many letters it does have? "))

word = ["_" for i in range(length)]
chances = length

while chances > 0:
    guess = random.choice(letters)
    letters.remove(guess)
    status = input(f'Does the word contain "{guess}"? ').lower()
    if status == "y":
        count = int(input(f'How many "{guess}" does it have? '))
        for i in range(count):
            index = int(input(f'Enter index of {guess}: '))
            word[index] = guess
    elif status == "n":
        chances -= 1
        continue
    if "_" not in word:
        break

if "_" in word:
    print("failed")
else:
    word = "".join(word)
    print(f'The word {word} crracked after {attempts} attempts')
