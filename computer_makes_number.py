import random

# Setting the number

numbers_available = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers_available_wo_0 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
guess_list = {}

guess_number = 0

def generate_random_number():
    number_to_guess = []
    first_digit = random.choice(numbers_available_wo_0)
    number_to_guess.append(str(first_digit))
    for digit in range(3):
        digit = random.choice(numbers_available)
        digit = str(digit)
        number_to_guess.append(digit)
    return number_to_guess


def check_guess_for_repeat_numbers(number_to_guess):
    check_guess = set(number_to_guess)
    if len(check_guess) == 4:
        return number_to_guess
    else:
        number_to_guess = "repeats"
        return number_to_guess


def printed_guess(number_to_guess):
    printed_guess = int(number_to_guess[0] + number_to_guess[1] + number_to_guess[2] + number_to_guess[3])
    return printed_guess

#  Processing guess


def check_if_guess_is_correct(guess):
    if guess == number_to_guess:
        guess = 'Correct'
    return guess


def return_cows_and_bulls(guess, number_to_guess):
    guess = str(guess)
    number_to_guess = str(number_to_guess)
    checking_guess = list(guess)
    number_to_guess = list(number_to_guess)
    cows = 0
    bulls = 0
    for i in range(len(checking_guess)):
        if checking_guess[i] in number_to_guess:
            if checking_guess[i] == number_to_guess[i]:
                bulls = bulls + 1
            else:
                cows = cows + 1

    return (cows, bulls)


def store_guess(guess, cows, bulls, guess_number):
    guess_number = guess_number + 1
    guess_list.update({f'guess{guess_number}': {'guess': guess, 'guess_cows': cows, 'guess_bulls': bulls}})
    return guess


# Script


number_to_guess = generate_random_number()
number_to_guess = check_guess_for_repeat_numbers(number_to_guess)
while number_to_guess == 'repeats':
    number_to_guess = generate_random_number()
    number_to_guess = check_guess_for_repeat_numbers(number_to_guess)
    if number_to_guess != 'repeats':
        break
number_to_guess = printed_guess(number_to_guess)
print("Enter your first guess: ")
guess = input()
correct_guess = check_if_guess_is_correct(guess)
if correct_guess == "Correct":
    print("Game has finished!")
else:
    cows, bulls = return_cows_and_bulls(guess, number_to_guess)
    store_guess(guess, cows, bulls, guess_number)
    for guess in guess_list:
        print(f"Print the guess name and then : {cows} cows and {bulls} bulls")

while guess != 'Correct':
    print("Enter another guess.")
    guess = input()
    correct_guess = check_if_guess_is_correct(guess)
    if correct_guess == "Correct":
        print("Game has finished!")
        break
    else:
        cows, bulls = return_cows_and_bulls(guess, number_to_guess)
        store_guess(guess, cows, bulls, guess_number)
        for guess in guess_list:
            print(f"Print the {guess} and then : {cows} cows and {bulls} bulls")
