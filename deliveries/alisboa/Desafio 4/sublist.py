"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 'sublist'
SUPERLIST = 'superlist'
EQUAL = 'equal'
UNEQUAL = 'unequal'


def sublist(list_one, list_two):
    # a = [element in list_two for element in list_one]
    # b = [element in list_one for element in list_two]
    if not list_one and list_two:
        return SUBLIST
    if not list_two and list_one:
        return SUPERLIST
    if list_one == list_two:
        return EQUAL

    # Check if all the elements in list_two are in list_one, and with the correct order
    for index in range(0, len(list_one)):
        if list_two[0] == list_one[index]:
            index_extern_for = index
            for index_j in range(0, len(list_two)):
                if list_two[index_j] != list_one[index_extern_for]:
                    break
                if index_j == len(list_two) - 1:
                    return SUPERLIST
                index_extern_for += 1
                if index_extern_for >= len(list_one):
                    break

    # Check if all the elements in list_one are in list_two, and with the correct order
    for index in range(0, len(list_two)):
        if list_one[0] == list_two[index]:
            index_extern_for = index
            for index_j in range(0, len(list_one)):
                if list_one[index_j] != list_two[index_extern_for]:
                    break
                if index_j == len(list_one) - 1:
                    return SUBLIST
                index_extern_for += 1
                if index_extern_for >= len(list_two):
                    break
    return UNEQUAL

