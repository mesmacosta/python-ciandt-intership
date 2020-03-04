import random


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


word = random.choice(HANGMAN_DATA)
print(word)
retorno = "_".join([char if char in " " else "" for char in word])
print(retorno)