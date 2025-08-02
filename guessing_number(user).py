import random

print("*** Welcome to Guessing Number ***")

def guess_number():
    print("Chosse a range number to guess")
    low = int(input("from: "))
    high = int(input("to: "))

    number = random.randint(low, high)
    attempts = 0
    while True:
        guess = int(input(f'Guess a number between {low} and {high}: '))
        attempts += 1

        if guess == number:
            break
        elif guess < number:
            print("Too low")
            low = guess + 1
        elif guess > number:
            print("Too high")
            high = guess - 1

    return attempts

attempts = guess_number()
print(f"Congradulations! You have it at {attempts} attempts.")


