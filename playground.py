import random

# Create your views here.
# https://www.geeksforgeeks.org/python-check-if-list-contains-all-unique-elements/

# Global data storage

guesses = {}
numbers_available = [1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers_not_available = []
numbers_definite = []
used_digits = []
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


def prompt_player_number():
    print("Put in the number for the computer to guess: ")
    number_to_guess = input()
    number_to_guess_digits = []
    for i in number_to_guess:
        number_to_guess_digits.append(i)
    flag = len(set(number_to_guess_digits)) == len(number_to_guess_digits)
    while flag is False:
        number_to_guess = input()
        number_to_guess_digits = []
        for i in number_to_guess:
            number_to_guess_digits.append(i)
        flag = len(set(number_to_guess_digits)) == len(number_to_guess_digits)
        if flag:
            break
    print("Your number is valid: " + str(number_to_guess))


def analysed_guess(numbers_available, numbers_definite):
    available_numbers = available_numbers(numbers_available, numbers_not_available, numbers_definite)
    priority_numbers = priority_numbers(available_numbers)
    guess = generating_guess(priority_numbers)
    guess = check_guess_for_repeat_numbers(guess, priority_numbers)
    guess = printed_guess(guess)
    guess = checking_guess_is_unique(guess)
    return guess


def available_numbers(numbers_available, numbers_not_available, numbers_definite):
    if numbers_definite:
        numbers_available = []
        for digit in range(4):
            digit = random.choice(numbers_definite)
            digit = str(digit)
            while digit in guess:
                digit = random.choice(numbers_definite)
                digit = str(digit)
                if digit not in guess:
                    break
            numbers_available.append(str(digit))
    return available_numbers


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


def check_guess_for_repeat_numbers(guess, priority_numbers):
    # check_guess = set(guess)
    # if len(check_guess) == 4:
    #     print("it is long enough")
    # # while digit in guess:
    # #     generating_guess(priority_numbers)
    return guess


def printed_guess(guess):
    printed_guess = int(guess[0]+guess[1]+guess[2]+guess[3])
    print(printed_guess)
    return printed_guess


def checking_guess_is_unique(guess):
    return guess

    # guess = []
    # for key in guesses.keys():
    #     if guesses[key]['score'] > 2:
    #         g = 1
    # print("This was a good choice")
            

    # # This is if we have found all the numbers

    # if numbers_definite:
    #     for digit in range(4):
    #         digit = random.choice(numbers_definite)
    #         digit = str(digit)
    #         while digit in guess:
    #             digit = random.choice(numbers_definite)
    #             digit = str(digit)
    #             if digit not in guess:
    #                 break
    #         guess.append(str(digit))
    #     return guess
    # else:

    #     # This is if there are numbers not yet used.

    #     if len(used_digits) < 10:
    #         while len(used_digits) < 10:
    #             digit = random.choice(numbers_available)
    #             digit = str(digit)
    #             if digit not in used_digits:
    #                 used_digits.append(digit)
    #                 guess.append(str(digit))
    #             if len(guess) > 3 or len(used_digits) == 10:
    #                 break
    #         if len(guess) < 4:
    #             num_need_to_fill_guess = 4 - len(guess)
    #             for i in range(num_need_to_fill_guess):
    #                 digit = random.choice(numbers_available)
    #                 while digit in guess:
    #                     digit = random.choice(numbers_available)
    #                     digit = str(digit)
    #                     if digit not in guess:
    #                         break
    #                 guess.append(str(digit))
    #     else:
    #     # This is if you haven't found definite and you've used all the numbers

    #         for digit in range(4):
    #             digit = random.choice(numbers_available)
    #             digit = str(digit)
    #             while digit in guess:
    #                 digit = random.choice(numbers_available)
    #                 digit = str(digit)
    #                 if digit not in guess:
    #                     break
    #             guess.append(str(digit))
    # return guess


# def checking_guess_is_unique(guess, printed_guesss):
#     for key in guesses.keys():
#         if guesses[key]['printed_guess'] == printed_guess:
#             unique_guess = True
#         else:
#             unique_guess = False
#     return unique_guess


def prompt_player_cows_and_bulls_info():
    print("enter the number of cows:")
    number_of_cows = input()
    print("enter the number of bulls:")
    number_of_bulls = input()
    return (number_of_cows, number_of_bulls)


def guess_analysis(guess, number_of_cows, number_of_bulls, numbers_available, numbers_not_available):
    number_of_cows = int(number_of_cows)
    number_of_bulls = int(number_of_bulls)
    score = (number_of_cows * 1) + (number_of_bulls * 1)
    if score == 4:
        for i in range(4):
            numbers_available = []
            numbers_definite.append(int(guess[i]))
            numbers_available.append(int(guess[i]))
    elif score == 0:
        numbers_available = []
        numbers_not_available = []
        for i in range(4):
            numbers_not_available.append(int(guess[i]))
        for j in range(0, 10):
            if j not in numbers_not_available:
                numbers_available.append(j)
    else:
        numbers_available = []
        for i in range(0, 10):
            if i not in numbers_not_available:
                numbers_available.append(i)
    matched_combo = '-'
    for key in combos.keys():
        if combos[key]['combo_value'] == score:
            matched_combo = key
    printed_guess = display_computer_guess(guess)
    guesses.update({f'guess_{x}': {
                        'first_no': guess[0],
                        'second_no': guess[1],
                        'third_no': guess[2],
                        'fourth_no': guess[3],
                        'cows': number_of_cows,
                        'bulls': number_of_bulls,
                        'score': score,
                        'printed_guess': printed_guess,
                        'combo': matched_combo
                   }})
    return (numbers_available, numbers_not_available)



def display_computer_guess(guess):
    printed_guess = int(guess[0]+guess[1]+guess[2]+guess[3])
    print(printed_guess)
    return printed_guess


def display_cow_and_bull_info(number_of_cows, number_of_bulls, printed_guess):
    print(f"There are {number_of_cows} cows and {number_of_bulls} bulls in {printed_guess}")


def assess_if_answer_is_correct(number_of_bulls):
    if number_of_bulls == "4":
        finished = True
        return finished
    else:
        finished = False
        return finished
# ----------------------------------------------------------------------------------------------------

# Script


prompt_player_number()
print("Computer's first guess")
# Turn this into a function and save repeating it all.
guess = analysed_guess(numbers_available, numbers_definite)
printed_guess = display_computer_guess(guess)
number_of_cows, number_of_bulls = prompt_player_cows_and_bulls_info()
display_cow_and_bull_info(number_of_cows, number_of_bulls, printed_guess)
# guess_analysis(guess, number_of_cows, number_of_bulls, numbers_available, numbers_not_available)
numbers_available, numbers_not_available = guess_analysis(guess, number_of_cows, number_of_bulls, numbers_available, numbers_not_available)
x = x + 1
finished = assess_if_answer_is_correct(number_of_bulls)

if finished:
    print("The computer guessed correctly!")
else:
    while finished is False:
        print("Okay, the computer guesses: ")

        guess = analysed_guess(numbers_available, numbers_definite)
        printed_guess = display_computer_guess(guess)
        unique_guess = checking_guess_is_unique(guess, printed_guess)
        while unique_guess:
            print("redoing guess")
            unique_guess = checking_guess_is_unique(guess, printed_guess)
            if unique_guess is False:
                break
        number_of_cows, number_of_bulls = prompt_player_cows_and_bulls_info()
        display_cow_and_bull_info(number_of_cows, number_of_bulls, printed_guess)
        # guess_analysis(guess, number_of_cows, number_of_bulls, numbers_available, numbers_not_available)
        numbers_available, numbers_not_available = guess_analysis(guess, number_of_cows, number_of_bulls, numbers_available, numbers_not_available)
        x = x + 1
        finished = assess_if_answer_is_correct(number_of_bulls)
        if finished:
            break
      


print("The computer guessed correctly!")
