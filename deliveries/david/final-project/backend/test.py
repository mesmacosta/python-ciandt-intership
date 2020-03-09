import random
import uuid
import re

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

id = uuid.uuid1().int
word = random.choice(HANGMAN_DATA)
# print(word)
find = "_".join([char if char in " " else "" for char in word])
list_find = list()
for concat in find:
	list_find.append(concat)
print(list_find)

game_start = {'game_id': id, 'data':
		{'word': word,
		 'find': find,
		 'traies': 0,
		 'result': ''
	}}


# retorno = [chave == 'data' in chave for chave in game_start.items() ]
palavra = game_start.get('data').get('word')
print(palavra)
print(len(palavra))
letter = input("Pass letter: ")

for index in range(0, len(palavra)):
	if letter in palavra[index].lower():
		alter = palavra[index]
		list_find[index] = alter


print(list_find)
