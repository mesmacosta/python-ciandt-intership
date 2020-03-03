import operator
import collections
list_one = [1, 2, 3]
list_two = [1, 2, 3]
list_all = list()

list_all.append(list_one)
list_all.append(list_two)
print(list_all)

list1 = collections.Counter(list_all)

# list1 = ','.join([str(l1) for l1 in list_one])
# list2 = ','.join([str(l2) for l2 in list_two])

# print(list1)

