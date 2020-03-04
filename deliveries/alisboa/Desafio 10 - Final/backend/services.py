import datetime
import uuid
import yaml
import json
import re

from random import choice, randint
from repository import save_game, new_game, get_game, delete_game

MAX_TRIES = 6

__all__ = ['start_game', 'gess_word', 'reset_game', 'new_id']


def gess_word(_id: str, gess: str):
	gess = gess.lower()
	current_game = get_game(_id)
	if current_game['result'] == 'win' or current_game['result'] == 'lose':
		return {
			'game_id': _id,
			'data': current_game
		}
	word_indexes = [pos for pos, char in enumerate(current_game['word'].lower()) if char == gess]
	find_list = list(current_game['find'])
	if len(word_indexes) > 0:
		for position in word_indexes:
			find_list[position] = gess
		current_game.pop('find')
		current_game['find'] = "".join(find_list)
		if __check_win(current_game['find']):
			current_game['result'] = 'win'
	else:
		current_game['tries'] += 1
		if current_game['tries'] >= MAX_TRIES:
			current_game['result'] = 'lose'

	saved_game = save_game(_id, current_game)
	return {
		'game_id': _id,
		'data': saved_game
	}


def __check_win(find):
	return all([char != '_' for char in find])


def new_id():
	return randint(10000000, 99999999)


def reset_game(_id):
	try:
		delete_game(_id)
		return {'success': True}
	except:
		return {'success': False}


def start_game(_id):
	word = choice(HANGMAN_DATA)
	find = "".join(['_' if char != ' ' else ' ' for char in word])
	game_created = new_game({
		_id: {
			'word': word,
			'find': find,
			'tries': 0,
			'result': ''
		}
	})
	return {
		'game_id': _id,
		'data': game_created[_id]
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