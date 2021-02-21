import random
import django.contrib.redirects
# Create your views here.
# https://www.geeksforgeeks.org/python-check-if-list-contains-all-unique-elements/

# Global data storage

guesses = {}




def prompt_player_number():
    print("Put in the number for the computer to guess: ")
    number_to_guess = input()
    number_to_guess_digits = []
    for i in number_to_guess:
        number_to_guess_digits.append(i)
    flag = len(set(number_to_guess_digits)) == len(number_to_guess_digits)
    while flag is False:
        print("Duplicates. Enter new number: ")
        number_to_guess = input()
        number_to_guess_digits = []
        for i in number_to_guess:
            number_to_guess_digits.append(i)
        flag = len(set(number_to_guess_digits)) == len(number_to_guess_digits)
        if flag:
            break
    print("Your number is valid: " + str(number_to_guess))






def computer_first_guess():
    # choosing first digit
    first_guess = []
    digit = random.randint(1,9)
    first_guess.append(str(digit))
    for digit in range(3):
        digit = random.randint(0,9)
        digit = str(digit)
        while digit in first_guess:
            digit = random.randint(0,9)
            digit = str(digit)
            if digit not in first_guess:
                break
        first_guess.append(str(digit))
    return first_guess


def display_computer_first_guess():
    first_guess = computer_first_guess()
    printed_first_guess = int(first_guess[0]+first_guess[1]+first_guess[2]+first_guess[3])
    print(printed_first_guess)
    return printed_first_guess


def prompt_player_cows_and_bulls_info():
    print("enter the number of cows:")
    number_of_cows = input()
    print("enter the number of bulls:")
    number_of_bulls = input()
    return (number_of_cows, number_of_bulls)


def display_cow_and_bull_info(number_of_cows, number_of_bulls, printed_first_guess):
    print(f"There are {number_of_cows} cows and {number_of_bulls} bulls in {printed_first_guess}")


def guess_analysis(first_guess, number_of_cows, number_of_bulls):
    guesses.update({'guess_1': {
                        'first_no': first_guess[0],
                        'second_no': first_guess[1],
                        'third_no': first_guess[2],
                        'fourth_no': first_guess[3],
                        'cows': number_of_cows,
                        'bulls': number_of_bulls
                   }})
    print(guesses)





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
first_guess = computer_first_guess()
printed_first_guess = display_computer_first_guess()
number_of_cows, number_of_bulls = prompt_player_cows_and_bulls_info()
display_cow_and_bull_info(number_of_cows, number_of_bulls, printed_first_guess)
finished = assess_if_answer_is_correct(number_of_bulls)
guess_analysis(first_guess, number_of_cows, number_of_bulls)
if finished:
    print("The computer guessed correctly!")
else:
    while finished is False:
        print("Okay, the computer guesses: ")
        display_computer_first_guess() # needs changing to subsequent guesses. 
        number_of_cows, number_of_bulls = prompt_player_cows_and_bulls_info()
        display_cow_and_bull_info(number_of_cows, number_of_bulls, printed_first_guess)
        # print("no. of bulls" + number_of_bulls)
        finished = assess_if_answer_is_correct(number_of_bulls)
        if finished:
            break

print("The computer guessed correctly!")

