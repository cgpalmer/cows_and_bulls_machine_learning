import random
# Global data storage

guesses = {}
numbers_available = [1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers_not_available = []
numbers_definite = []
used_digits = []
guess = []
x = 1

# Intermediate combos
combos = {
    'combo_1': {
        'num_cows': 1,
        'num_bulls': 0,
        'combo_value': 1
    },
    'combo_2': {
        'num_cows': 0,
        'num_bulls': 1,
        'combo_value': 1
    },
    'combo_3': {
        'num_cows': 2,
        'num_bulls': 0,
        'combo_value': 2
    },
    'combo_4': {
        'num_cows': 0,
        'num_bulls': 2,
        'combo_value': 2
    },
    'combo_5': {
        'num_cows': 1,
        'num_bulls': 1,
        'combo_value': 2
    },
    'combo_6': {
        'num_cows': 3,
        'num_bulls': 0,
        'combo_value': 3
    },
    'combo_7': {
        'num_cows': 0,
        'num_bulls': 3,
        'combo_value': 3
    },
    'combo_8': {
        'num_cows': 2,
        'num_bulls': 1,
        'combo_value': 3
    },
    'combo_9': {
        'num_cows': 1,
        'num_bulls': 2,
        'combo_value': 3
    }
}

# Code for player interaction


def prompt_player_number():
    print("Put in the number for the computer to guess: ")
    number_to_guess = input()
    number_to_guess_digits = []
    for i in number_to_guess:
        number_to_guess_digits.append(i)
        # call to check not repeats function here.
    print("Your number is valid: " + str(number_to_guess))


def prompt_player_cows_and_bulls_info():
    print("enter the number of cows:")
    number_of_cows = input()
    print("enter the number of bulls:")
    number_of_bulls = input()
    return (number_of_cows, number_of_bulls)

# Code to choose a guess


def available_numbers(numbers_available, numbers_not_available, numbers_definite):
    if numbers_definite:
        numbers_available = []
        for digit in range(4):
            digit = random.choice(numbers_definite)
            digit = str(digit)
            numbers_available.append(str(digit))
    return numbers_available


def priority_numbers(available_numbers):
    priority_numbers = available_numbers
    return priority_numbers


def generating_guess(priority_numbers):
    guess = []
    for digit in range(4):
        digit = random.choice(priority_numbers)
        digit = str(digit)
        guess.append(digit)
    return guess


def check_guess_for_repeat_numbers(guess):
    check_guess = set(guess)
    if len(check_guess) == 4:
        return guess
    else:
        guess = "repeats"
        return guess


def printed_guess(guess):
    printed_guess = int(guess[0]+guess[1]+guess[2]+guess[3])
    print(printed_guess)
    return printed_guess


def checking_guess_is_unique(guess):
    if guesses:
        for prev_guess in guesses:
            unique_val = prev_guess['guess']
            print(unique_val)
    else:
        print("This is the first guess so obvs unique")
    return guess


def analysed_guess():
    guess = generating_guess(priority_numbers)
    guess = check_guess_for_repeat_numbers(guess)
    
    while guess == 'repeats':
        guess = generating_guess(priority_numbers)
        guess = check_guess_for_repeat_numbers(guess)
        if guess != 'repeats':
            break
    guess = printed_guess(guess)
    guess = checking_guess_is_unique(guess)
    print(guess)
    return guess


# End of guess code --------------------------------------------------------------------------

# Code to analyse the result from the guess

def process_cows_bulls_score(guess, number_of_cows, number_of_bulls):
    return score


def process_number_position(guess):
    return first_position, second_position, third_position, fourth_position


def create_new_numbers_lists(guess, numbers_available, numbers_definite, numbers_not_available, first_position, second_position, third_position, fourth_position):
    return numbers_available, numbers_definite, numbers_not_available


def store_guess_info(guess, score, numbers_available, numbers_definite, numbers_not_available, first_position, second_position, third_position, fourth_position):
    return guess


def guess_analysis(guess, number_of_cows, number_of_bulls, numbers_available, numbers_definite, numbers_not_available):
    score = process_cows_bulls_score(guess, number_of_cows, number_of_bulls)
    first_position, second_position, third_position, fourth_position = process_number_position(guess)
    numbers_available, numbers_definite, numbers_not_available = create_new_numbers_lists(guess, numbers_available, numbers_definite, numbers_not_available, first_position, second_position, third_position, fourth_position)
    store_guess_info(guess, score, numbers_available, numbers_definite, numbers_not_available, first_position, second_position, third_position, fourth_position)



# End of analysis code -----------------------------------------------------------------------

# Script to execute code

prompt_player_number()
print("Computer's first guess")
available_numbers = available_numbers(numbers_available, numbers_not_available, numbers_definite)
print(available_numbers)
priority_numbers = priority_numbers(available_numbers)
number_of_cows, number_of_bulls = prompt_player_cows_and_bulls_info(guess)
guess_analysis(guess, number_of_cows, number_of_bulls, numbers_available, numbers_definite, numbers_not_available)



# End of script

