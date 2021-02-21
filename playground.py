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
    guess = []
    if numbers_definite:
        for digit in range(4):
            digit = random.choice(numbers_definite)
            digit = str(digit)
            while digit in guess:
                digit = random.choice(numbers_definite)
                digit = str(digit)
                if digit not in guess:
                    break
            guess.append(str(digit))
        return guess
    else:
        if len(used_digits) < 10:
            while len(used_digits) < 10:
                digit = random.choice(numbers_available)
                digit = str(digit)
                if digit not in used_digits:
                    used_digits.append(digit)
                    guess.append(str(digit))
                if len(guess) > 3 or len(used_digits) == 10:
                    break
            if len(guess) < 4:
                num_need_to_fill_guess = 4 - len(guess)
                for i in range(num_need_to_fill_guess):
                    digit = random.choice(numbers_available)
                    while digit in guess:
                        digit = random.choice(numbers_available)
                        digit = str(digit)
                        if digit not in guess:
                            break
                    guess.append(str(digit))
        else:
            for digit in range(4):
                digit = random.choice(numbers_available)
                digit = str(digit)
                while digit in guess:
                    digit = random.choice(numbers_available)
                    digit = str(digit)
                    if digit not in guess:
                        break
                guess.append(str(digit))

        for key in guesses.keys():
            print(key, '->', guesses[key])
        return guess


def prompt_player_cows_and_bulls_info():
    print("enter the number of cows:")
    number_of_cows = input()
    print("enter the number of bulls:")
    number_of_bulls = input()
    return (number_of_cows, number_of_bulls)


def guess_analysis(guess, number_of_cows, number_of_bulls, numbers_available, numbers_not_available):
    number_of_cows = int(number_of_cows)
    number_of_bulls = int(number_of_bulls)
    score = (number_of_cows * 1) + (number_of_bulls * 10)
    if score == 40 or score == 31 or score == 22 or score == 13 or score == 4:
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

    printed_guess = display_computer_guess(guess)
    guesses.update({f'guess_{x}': {
                        'first_no': guess[0],
                        'second_no': guess[1],
                        'third_no': guess[2],
                        'fourth_no': guess[3],
                        'cows': number_of_cows,
                        'bulls': number_of_bulls,
                        'score': score,
                        'printed_guess': printed_guess
                   }})
    print(guesses)
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
        print(numbers_available)
        guess = analysed_guess(numbers_available, numbers_definite)
        printed_guess = display_computer_guess(guess)
        number_of_cows, number_of_bulls = prompt_player_cows_and_bulls_info()
        display_cow_and_bull_info(number_of_cows, number_of_bulls, printed_guess)
        # guess_analysis(guess, number_of_cows, number_of_bulls, numbers_available, numbers_not_available)
        numbers_available, numbers_not_available = guess_analysis(guess, number_of_cows, number_of_bulls, numbers_available, numbers_not_available)
        x = x + 1
        finished = assess_if_answer_is_correct(number_of_bulls)
        if finished:
            break

print("The computer guessed correctly!")
