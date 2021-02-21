import random
import django.contrib.redirects
# Create your views here.
# https://www.geeksforgeeks.org/python-check-if-list-contains-all-unique-elements/
def prompt_player_number():
    print("Put in the number for the computer to guess: ")
    number_to_guess = input()
    number_to_guess_digits = []
    for i in number_to_guess:
        number_to_guess_digits.append(i)
        print(number_to_guess_digits)
    flag = len(set(number_to_guess_digits)) == len(number_to_guess_digits)
    print(flag)
    while flag is False:
        print("Duplicates. Enter new number: ")
        number_to_guess = input()
        number_to_guess_digits = []
        for i in number_to_guess:
            number_to_guess_digits.append(i)
            print(number_to_guess_digits)
        flag = len(set(number_to_guess_digits)) == len(number_to_guess_digits)
        if flag:
            break
    print("suitable number found")
    print("Your number is valid: " + str(number_to_guess))





first_guess = []
def computer_first_guess():
    for digit in range(4):
        digit = random.randint(0,9)
        first_guess.append(str(digit))
    printed_first_guess = int(first_guess[0]+first_guess[1]+first_guess[2]+first_guess[3])
    print(printed_first_guess)


def display_computer_first_guess():
    print("computers first guess")
    computer_first_guess()

def prompt_player_cows_and_bulls_info():
    print("enter the number of cows:")
    number_of_cows = input()
    print("enter the number of bulls:")
    number_of_bulls = input()
    return (number_of_cows, number_of_bulls)


def display_cow_and_bull_info(number_of_cows, number_of_bulls,):
    printed_first_guess = int(first_guess[0]+first_guess[1]+first_guess[2]+first_guess[3])
    print(printed_first_guess)
    print(f"There are {number_of_cows} cows and {number_of_bulls} bulls in {printed_first_guess}")


prompt_player_number()
display_computer_first_guess()
number_of_cows, number_of_bulls = prompt_player_cows_and_bulls_info()
display_cow_and_bull_info(number_of_cows, number_of_bulls,)
