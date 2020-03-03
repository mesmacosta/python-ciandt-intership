list_circulation = [[],[],[],[],[],[],[]]
write = ["1","2","3"]

# for numbers in write:
#     ','.join(str(list_circulation(numbers)))

for indice, item in enumerate(list_circulation):
    list_circulation[indice] = write


print(list_circulation)


# def eg1_for(matriz):
#    flat = []
#    for row in matriz:
#       for x in row:
#          flat.append(x)
#    return flat
#
# def eg1_cl(matriz):
#    return [x for row in matriz for x in row]