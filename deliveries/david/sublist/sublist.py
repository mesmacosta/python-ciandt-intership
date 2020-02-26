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
SUBLIST = "sublist"
SUPERLIST = "superlist"
EQUAL = "equal"
UNEQUAL = "unequal"


def sublist(list_one, list_two):

    if list_one == list_two:
        return EQUAL
    for firest_empty in list_one:
        for second_two in list_two:
            # if list_one
            pass

    # elif list_one == None and list_one < list_two:
    #     return SUBLIST
    # elif list_one >= list_two:
    #     return SUPERLIST
    # elif list_one != list_two:
    #     return UNEQUAL

sublist([1, 2, 4], [1, 2, 4])


