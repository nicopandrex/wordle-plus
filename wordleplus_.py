"""
Nico Lippiatt-Cook
Birch Saccamango
CS1210
Wordle Plus
"""

import random

import time

from colorama import Fore, Back, Style


ALPHA = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
         'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
         's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def validator(x):
    try:
        if len(x) == 5:
            for letter in x:
                if letter.lower() in ALPHA:
                    with open("valid-wordle-words.txt") as f:
                        words = f.read()
                        if x.lower() in words:
                            return True
        return False
    except SyntaxError:
        return False
    except TypeError:
        return False


def get_word():
    with open("word_list.txt") as f:
        words = f.readlines()
        return random.choice(words)

def formater(guess):
    result = []
    for a in guess:
        result.append([a, 0])
    return result


def checker(guess, target):
    placeholder = [['!', 0], ['!', 0], ['!', 0], ['!', 0], ['!', 0]]
    target = list(target)
    for i, letter in enumerate(guess):
        if letter[0] in target:
            if letter[0] == target[i]:
                placeholder[i] = [letter[0], 2]
                guess[i] = ['!', 0]
                target[i] = '&'

    for i, letter in enumerate(guess):
        if letter[0] in target:
            placeholder[i] = [letter[0], 1]
            guess[i] = ['!', 0]
            for e, l in enumerate(target):
                if l == letter[0]:
                    target[e] = '&'
                    break

    for i, letter in enumerate(placeholder):
        if letter[0] != '!':
            guess[i] = placeholder[i]

    return guess


def printer(lst):
    for x in lst:
        if x[1] == 0:
            print(Fore.WHITE + Back.BLACK +
                  '\033[1m' + x[0].upper(), end="")
        elif x[1] == 1:
            print(Fore.WHITE + Back.YELLOW +
                  '\033[1m' + x[0].upper(), end="")
        elif x[1] == 2:
            print(Fore.WHITE + Back.GREEN +
                  '\033[1m' + x[0].upper(), end="")
    print(Style.RESET_ALL + '\n')


def printer_end(lst):
    for x in lst:
        if x[1] == 0:
            print(Fore.WHITE + Back.BLACK +
                  '\033[1m' + x[0].upper(), end="")
        elif x[1] == 1:
            print(Fore.WHITE + Back.YELLOW +
                  '\033[1m' + x[0].upper(), end="")
        elif x[1] == 2:
            print(Fore.WHITE + Back.GREEN +
                  '\033[1m' + x[0].upper(), end="")
    print(Style.RESET_ALL)


def key_printer(lst):
    for i, row in enumerate(lst):
        if i == 1:
            print(' ', end='')
        elif i == 2:
            print('  ', end='')
        for x in row:
            if x[1] == 0:
                print(Fore.WHITE + Back.BLACK +
                      '\033[1m' + x[0].upper(), end="")
            elif x[1] == 1:
                print(Fore.WHITE + Back.YELLOW +
                      '\033[1m' + x[0].upper(), end="")
            elif x[1] == 2:
                print(Fore.WHITE + Back.GREEN +
                      '\033[1m' + x[0].upper(), end="")
            elif x[1] == 3:
                print(Fore.BLACK + Back.WHITE +
                      '\033[1m' + x[0].upper(), end="")
        print(Style.RESET_ALL)
    print(Style.RESET_ALL + '\n')


def keyboard_update(keyboard, guess):
    for i, l in enumerate(guess):
        for row in keyboard:
            for i, letter in enumerate(row):
                if l[0] == letter[0]:
                    if letter[1] != 2:
                        letter[1] = l[1]
    return keyboard


if __name__ == '__main__':
    print("Welcome to Wordle Plus! We have choosen a random " \
          "five letter word and you must\n" \
          "guess it! For each guess you make, the letters in your word will\n"
          "be colored yellow if they are in the word " \
          "but not in the right spot, green if \n"
          "they are in the right spot, and grey if they are not in the word. "\
          "A corresponding \n"
          "keyboard layout will be printed with that "\
          "same information every guess. \n"
          "You have six guesses.")
    playing = True
    while playing == True:
        print("Make your first guess:\n")
        keyboard = [[['q', 3], ['w', 3], ['e', 3], ['r', 3],
                     ['t', 3], ['y', 3], ['u', 3], ['i', 3],
                     ['o', 3], ['p', 3]], [['a', 3], ['s', 3],
                    ['d', 3], ['f', 3], ['g', 3], ['h', 3], ['j', 3],
                    ['k', 3], ['l', 3]], [['z', 3], ['x', 3], ['c', 3],
                    ['v', 3], ['b', 3], ['n', 3], ['m', 3]]]

        target = get_word()
        guesses = 0
        guesses_real = 0
        guessed = []
        while guesses < 6:
            response = input('')
            if validator(response):
                if guesses == 0:
                    start = time.time()
                correct = 0
                response.lower()
                response = formater(response)
                guess = checker(response, target)
                printer(guess)
                keyboard_update(keyboard,
                                checker(response, target))
                key_printer(keyboard)
                guessed.append(guess)
                guesses += 1
                guesses_real += 1

                for e in guess:
                    if e[1] == 2:
                        correct += 1
                    else:
                        pass
                if correct == 5:
                    guesses = 10
                    end = time.time()
                if guesses == 5:
                    end = time.time()

            else:
                print("Invalid Input")

        if guesses == 10:
            print(f"Congratulations you have won! The word was {target}"
                  f"and you guessed it in {guesses_real} guess(es)! "\
                  f"It took you {(end - start):.0f}\n"
                  f"seconds to win! Here is an aesthetically pleasing recap \n"
                  f"of your game. Thanks for playing!\n")
            for e in guessed:
                printer_end(e)
            while True:
                play_again = input("Would you like to play again? (y/n): ")
                if play_again.lower() == "y":
                    playing = True
                    guesses = 0
                    break
                elif play_again.lower() == "n":
                    playing = False
                    break
                else:
                    print("Invalid Response")
                    pass
        else:
            print(f"Unfortunatly you lose. The word was {target}"
                  f"and you played for {(end - start):.0f} seconds. Here is\n"
                  f"an aesthetically pleasing recap of your game.\n"
                  f"Thanks for playing!\n")
            for e in guessed:
                printer_end(e)
            while True:
                play_again = input("Would you like to play again? (y/n): ")
                if play_again.lower() == "y":
                    playing = True
                    break
                elif play_again.lower() == "n":
                    playing = False
                    break
                else:
                    print("Invalid Response")
                    pass