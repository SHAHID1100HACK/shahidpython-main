import random

# Prompt user for a valid level (positive integer)
while True:
    try:
        level = int(input("Level: "))
        if level > 0:
            break
    except ValueError:
        pass  # Ignore invalid input and loop again

# Generate random number between 1 and level
number = random.randint(1, level)

# Prompt user to guess the number
while True:
    try:
        guess = int(input("Guess: "))
        if guess < 1:
            continue
    except ValueError:
        continue

    if guess < number:
        print("Too small!")
    elif guess > number:
        print("Too large!")
    else:
        print("Just right!")
        break
