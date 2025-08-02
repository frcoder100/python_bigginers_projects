import random

print("Random Number Generator")

def random_number_generator():
    start = int(input("from: "))
    end = int(input("to: "))

    while True:
        print(random.randint(start, end))

        status = input("print q to quit | press enter to continue | press tab to change the range: ").lower()
        if status == "q":
            break
        elif status == '\n':
            continue
        elif status == '\t':
            random_number_generator()
            break

random_number_generator()

