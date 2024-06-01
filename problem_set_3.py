import random

def get_random_int(min_val, max_val):
    return random.randint(min_val, max_val)

def get_guess(max_value):
    random_int = get_random_int(1, max_value)
    try:
        user_guess = int(input(f"Guess a number between 1 and {max_value}: "))
        if 1 <= user_guess <= max_value:
            return True if user_guess == random_int else False
        else:
            return -1
    except ValueError:
        return -1

def play_game():
    max_guesses = 4
    correct_guesses = 0
    for _ in range(max_guesses):
        result = get_guess(5)
        if result == -1:
            print("Invalid response!")
            return
        elif result:
            print("Correct!")
            correct_guesses += 1
        else:
            print("Wrong!")
    print(f"You guessed {correct_guesses / max_guesses * 100:.0f}% of the random numbers correctly.")
