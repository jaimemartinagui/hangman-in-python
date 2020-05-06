"""Hangman"""

import turtle
from time import sleep
from operator import setitem
from itertools import count

import numpy as np

from draw import draw_hangman

def hangman():
    """Main function of the game"""

    t = turtle.Turtle()
    turtle.Screen().setup(1000, 1000)
    menu()
    mode = input("Escoja la dificultad del juego (1 -> estándar; 2 -> difícil): ")
    while mode != "1" and mode != "2":
        mode = input("\nIntroduzca 1 para modo estándar y 2 para modo difícil: ")
    filename = "words_lvl{}.txt".format(mode)
    word = select_random_word(filename)
    # Initialize some variables
    lives, score, correct_letters, used_letters = 7, 0, 0, []
    for it in count():
        if it == 0:
            clue = ["_"] * len(word)
            show_clue(lives, score, clue)
        letter = input("\nIntroduzca una letra: ").lower()
        while letter in used_letters:
            letter = input("\nLa letra introducida ya se ha probado antes. Introduzca otra letra: ")
        used_letters.append(letter)
        if letter in word:
            score += 2
            pos = [pos for pos, char in enumerate(word) if char == letter]
            for idx in pos:
                setitem(clue, idx, letter)
            correct_letters += len(pos)
            if correct_letters >= len(word):
                correct_answer(word, score)
                turtle.Screen().bye()
                break
        else:
            lives -= 1
            t.reset()
            t.speed(10)
            t.hideturtle()
            draw_hangman(t, lives)
            if lives == 0:
                print("\nGame Over!\n")
                sleep(3)
                turtle.Screen().bye()
                break
            score = max(0, score - 1)
        show_clue(lives, score, clue)
        solve = input("\n¿Desea resolver? (y/n): ")
        while solve.lower() not in ['y', 'n']:
            solve = input("¿Desea resolver? (y/n): ")
        if solve.lower() == 'y':
            if input("\nIntroduzca una palabra: ").lower() == word.lower():
                correct_answer(word, score)
                turtle.Screen().bye()
                break
            else:
                print("\nLa palabra no es correcta. Fin del juego!\n")
                sleep(3)
                turtle.Screen().bye()
                break


def correct_answer(word, score):
    print("\n")
    print("       ", end="", flush=True)
    for letter in word:
        sleep(0.2)
        print(letter + " ", end="", flush=True)
    print("\n\n       Correcto!!")
    print("\nEnhorabuena! Su puntación final es de {} puntos.\n".format(score + 10))


def show_clue(lives, score, clue):
    print('\n       Lives:', lives)
    print('       Score:', score)
    print("\n       " + " ".join(clue))


def select_random_word(filename):
    """Fuction that selects a random word from the txt file"""

    path = "/".join(["words_files", filename])
    with open(path) as file:
        words_list = file.read().splitlines()
    rand_idx = np.random.randint(low=0, high=50)
    return words_list[rand_idx]


def menu():
    """Funcion to show the game instructions"""

    print("\nBienvenido a Hangman!!")
    print("\n             Instrucciones de juego")
    print("             ----------------------")
    print("- El jugador tiene 7 oportunidades por palabra.")
    print("- Solo los fallos restan oportunidades.")
    print("- Si acierta letra suma 2 puntos.")
    print("- Si falla letra resta 1 punto.")
    print("- Si resuelve antes de gastar las 7 oportunidades suma 10 puntos.")
    print("\n                 A jugar!!!\n")

