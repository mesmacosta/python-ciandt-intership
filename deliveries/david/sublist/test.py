import operator
list_one = []
list_two = [1, 2, 3]

result = any(map(operator.eq, list_one, list_two))
print(result)

# resultado = [list1 == list2 for list1 in list_one for list2 in list_two]
# # resultado = [(list1, list2) for list1 in list_one for list2 in list_two]
#
# print(resultado)
#
# users = [{'name': 'Miguel', 'age': 31}, {'name': 'max', 'age': 30}]
# user_name = [user['age'] for user in users]
# print(user_name)

# squares = list()
# for i in range(1, 101):
#     squares.append(i*2)
# print(squares)
#
# squares2 = [i*2 for i in range(1, 101)]
# print(squares2)
#
# movies = ["Star Wars", "Gandhi", "Casablaca", "Shawshank Redmption", "Toy Store",
#           "Gone with ind", "Rear Window", "To kill A Mockingbird, 1981"]
#
# gmovies = []
# gmovies = [titles for titles in movies if titles.startswith("R")]
# print(gmovies)
#
# pre2k = [title for (title, year) in movies if year < 2000]
# print(pre2k)