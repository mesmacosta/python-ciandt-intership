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
    right_word = ''
    word = get_game(_id)
    logging.info(f'Passou aqui', {word})
    # if gess in word:
    #     right_word = word
    return {right_word, _id}


def new_id():
    return randint(100000, 999999)


def reset_game(_id):
    return 'success'


def start_game(_id):
    word = choice(HANGMAN_DATA)
    find = "_".join([char if char in " " else "" for char in word])
    game_start = {'game_id': _id,
                  'data':
                      {'word': word,
                       'find': find,
                       'tries': 0,
                       'result': ''
                       }}
    return new_game(game_start)


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
