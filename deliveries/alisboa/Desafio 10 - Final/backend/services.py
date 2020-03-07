import unicodedata
import time
import re

from random import choice, randint
from repository import save_game, new_game, get_game, delete_game

MAX_TRIES = 6
MAX_TIME = 100  # SECONDS
__all__ = ['start_game', 'gess_word', 'reset_game', 'new_id']


def gess_word(_id: str, gess: str):
	if _id is None or not _id:
		return {'error': 'game_id should be passed'}, 400
	if gess is None:
		return {'error': 'guess must not be null'}, 400
	if len(gess) != 1:
		return {'error': 'guess must have 1 character'}, 400
	gess = gess.lower()
	gess = re.sub("[\u0300-\u036f]", "", unicodedata.normalize('NFD', gess))  # remove accentuation of gess
	current_game, session = get_game(_id)
	if __has_time_ended(current_game):
		current_game.result = 'lose'
	else:
		if not(current_game.result == 'win' or current_game.result == 'lose'):  # Game not ended
			word_indexes = [pos for pos, char in enumerate(current_game.word.lower())
							if re.sub("[\u0300-\u036f]", "", unicodedata.normalize('NFD', char)) == gess]
			find_list = list(current_game.find)
			if len(word_indexes) > 0:
				for position in word_indexes:
					find_list[position] = current_game.word[position]
				current_game.find = "".join(find_list)
				if __check_win(current_game.find):
					current_game.result = 'win'
			else:
				current_game.tries += 1
				if current_game.tries >= MAX_TRIES:
					current_game.result = 'lose'

	saved_game = save_game(_id, current_game, session)

	return ({
		'game_id': saved_game.id,
		'data': {
			'word': saved_game.word if saved_game.result == 'win' or saved_game.result == 'lose' else None,
			'find': saved_game.find,
			'tries': saved_game.tries,
			'result': saved_game.result,
			'time_sec': saved_game.time_sec,
			'date': saved_game.date
		}
	}, 200)


def __has_time_ended(game):
	time_now = time.time()
	if time_now - float(game.time_sec) > MAX_TIME:
		return True
	return False

def __check_win(find):
	return all([char != '_' for char in find])


def new_id():
	return randint(10000000, 99999999)


def reset_game(_id):
	try:
		delete_game(_id)
		return {'success': True}, 200
	except:
		return {'success': False}, 400


def start_game(_id):
	if not _id:
		return {
			'data': {
				'status': 'invalid id'
			}
		}, 400
	word = choice(HANGMAN_DATA)
	find = "".join(['_' if char != ' ' else ' ' for char in word])
	game_created = new_game({
		'id': _id,
		'word': word,
		'find': find,
		'tries': 0,
		'result': '',
		'time_sec': time.time(),
		'date': time.asctime()
	})
	game_created.pop('word')
	return {
		'game_id': _id,
		'data': game_created
	}, 200


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