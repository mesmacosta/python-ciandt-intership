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
SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4


def compare_list(list_one, list_two, _type):

    if list_one == list_two:
        return EQUAL
    list_two_matrix = []

    for item in range(0, len(list_two)):
        if item + len(list_one) <= len(list_two):
            list_two_matrix.append(list_two[item: item + len(list_one)])

    if list_one in list_two_matrix:
        return _type
    return None


def sublist(list_one, list_two):

    res = compare_list(list_one, list_two, SUBLIST)

    if res:
        return res
    res = compare_list(list_two, list_one, SUPERLIST)
    if res:
        return res
    return UNEQUAL
