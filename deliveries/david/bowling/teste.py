rolls = [6, 5, 3, 7, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

soma = 0
# for r in rolls:
#     soma += r
# for twice in range(0, 3):
#     soma +=rolls[twice]
# if soma == 10:
#     rolls[2] *= 2
#     print(rolls)
# # print(twice)
# print(rolls)
# print(rolls[0])
# row = [i for i in rolls]
# print(rolls)
for iterator in range(0, len(rolls)):
    soma += rolls[iterator]
    if soma == 10:
        change = rolls[iterator+1]*2
        rolls[iterator+1] = change
print(rolls)