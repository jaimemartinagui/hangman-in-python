"""Auxiliar functions"""

from time import sleep

import numpy as np


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
