# Guess the number by computer
import random


def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != "c":
        if low != high:
            guessNum = random.randint(low, high)
        else:
            guessNum = low
        feedback = input(
            f"Is {guessNum} too high (H), too low (L), or correct (C)? ").lower()
        if feedback == 'h':
            high = guessNum - 1
        elif feedback == 'l':
            low = guessNum + 1

    print(f"Yesss! The computer guessed your number, {guessNum}, correctly!")


computer_guess(300)
