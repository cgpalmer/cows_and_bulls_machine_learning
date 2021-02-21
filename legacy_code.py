# def computer_first_guess():
#     # choosing first digit
#     first_guess = []
#     digit = random.randint(1,9)
#     first_guess.append(str(digit))
#     for digit in range(3):
#         digit = random.randint(0,9)
#         digit = str(digit)
#         while digit in first_guess:
#             digit = random.randint(0,9)
#             digit = str(digit)
#             if digit not in first_guess:
#                 break
#         first_guess.append(str(digit))
#     return first_guess


# def display_computer_first_guess():
#     first_guess = computer_first_guess()
#     printed_first_guess = int(first_guess[0]+first_guess[1]+first_guess[2]+first_guess[3])
#     print(printed_first_guess)
#     return printed_first_guess


# def display_cow_and_bull_info(number_of_cows, number_of_bulls, printed_first_guess):
#     print(f"There are {number_of_cows} cows and {number_of_bulls} bulls in {printed_first_guess}")