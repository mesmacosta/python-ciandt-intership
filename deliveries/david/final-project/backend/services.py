import datetime
import uuid
import yaml
import json
import re
import logging

from random import randint, random, choice

from repository import save_game, game, get_game

MAX_TRIRES = 6

__all__ = ['start_game', 'gess_word', 'reset_game']




def gess_word(_id: str, gess: str):
    list_find = list()
    gess_lower = gess.lower()
    result = ''

    game = get_game(_id)
    word = game.get('word').lower()
    count_tries = game.get('tries')

    for p in game.get('find'):
        list_find.append(p[:])

    if gess_lower in word:
        validate_guess_and_return_word(gess_lower, word, list_find)
        if game.get('find') == word:
            result = 'win'
    else:
        count_tries += 1
        if count_tries == 6:
            result = 'lose'

    result_gess = {
            'word': word,
            'find': "".join(list_find),
            'tries': count_tries,
            'result': result
    }

    save_game(_id, result_gess)

    return {
        "game_id": _id,
        'data': result_gess
    }


def validate_guess_and_return_word(gess, word, list_find):

    for index in range(0, len(word)):
        if gess == word[index]:
            letter = word[index]
            list_find[index -1] = letter
    return list_find


def new_id():
    return uuid.uuid4()


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
        'data': game(game_start)[_id]
    }

HANGMAN_DATA = [
    "Alura",
    # "Business Complexity Points",
    # "Driven by Impact",
    # "Drupalize me",
    # "Gestão Financeira",
    # "Financial Management",
    # "Gemba Walk Data driven mindset",
    "Hoshin Kanri",
    # "Lean Digital Transformation",
    # "Introduction to Lean Leadership",
    # "Lifelong Learning",
    # "Mindset Data Driven",
    "O Reilly",
    "Pluralsight"
    # "Jira Poka Yoke",
    # "Powerful Stories Bradesco Seguros",
    # "Powerful Stories Cielo",
    # "Powerful Stories iHeartMedia",
    # "Powerful Stories Konica Minolta",
    # "Powerful Stories Porto Seguro",
    # "Powerful Stories Raizen",
    # "Powerful Stories VIVO",
    # "Introduction to Product Management",
    # "Our Unfinished Journey",
    # "Journey and Ambiguity",
    # "Lean Startup Week"
]
