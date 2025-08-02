import random

print("*** Welcome to Guessing Number Game! ***")

def guessing_number():
    print("Choose a range number for computer to guesss")
    low = int(input("from: "))
    high = int(input("to: "))

    attempts = 0
    while True:
        guess = random.randint(low, high)
        attempts += 1
        answer = input(f"Computer guess {guess} is it correct, low or high (c / l / h)? ").lower()

        if answer == "c":
            break
        elif answer == "l":
            low = guess + 1
        elif answer == "h":
            high = guess - 1

    return attempts, guess

attempts, guess = guessing_number()
print(f'Chosen number {guess} had guess after {attempts} attempts')