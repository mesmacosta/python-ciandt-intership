import datetime
import uuid
import yaml
import json
import re
import logging

from random import randint, random, choice

from repository import save_game, new_game, get_game

MAX_TRIRES = 6

__all__ = ['start_game', 'gess_word', 'reset_game']




def gess_word(_id: str, gess: str):
    list_find = list()
    count_tries = 0

    game = get_game(_id)
    word = game.get('word')

    for p in game.get('find'):
        list_find.append(p)

    validate_guess_and_return_word(gess, word, list_find)

    result_gess = {_id:
        {
            'word': word,
            'find': list_find,
            'tries': count_tries,
            'result': ''
        }
    }


    return {
        "game_id": _id,
        'data': result_gess[_id]
    }

def validate_guess_and_return_word(gess, word, list_find):

    for index in range(0, len(word)):
        if gess.lower() in word[index]:
            letter = word[index]
            list_find[index] = letter

def new_id():
    return randint(100000, 999999)


def reset_game(_id):
    return 'success'


def start_game(_id):
    word = choice(HANGMAN_DATA)
    find = "_".join([char if char in " " else "" for char in word])
    game_start = {_id:
        {
            'word': word,
            'find': find,
            'tries': 0,
            'result': ''
        }
    }

    return {
        'game_id': _id,
        'data': new_game(game_start)[_id]
    }

HANGMAN_DATA = [
    "Alura",
    "Business Complexity Points",
    "Driven by Impact",
    "Drupalize me",
    "Gestão Financeira",
    "Financial Management",
    "Gemba Walk Data driven mindset",
    "Hoshin Kanri",
    "Lean Digital Transformation",
    "Introduction to Lean Leadership",
    "Lifelong Learning",
    "Mindset Data Driven",
    "O Reilly",
    "Pluralsight",
    "Jira Poka Yoke",
    "Powerful Stories Bradesco Seguros",
    "Powerful Stories Cielo",
    "Powerful Stories iHeartMedia",
    "Powerful Stories Konica Minolta",
    "Powerful Stories Porto Seguro",
    "Powerful Stories Raizen",
    "Powerful Stories VIVO",
    "Introduction to Product Management",
    "Our Unfinished Journey",
    "Journey and Ambiguity",
    "Lean Startup Week"
]
