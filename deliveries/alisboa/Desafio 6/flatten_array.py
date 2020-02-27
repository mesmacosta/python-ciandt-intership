def flatten(iterable):
    flatten_list = []
    for element in iterable:
        if type(element) == list:
            # If element is a list, the function recursive calls itself
            flatten_list.extend(flatten(element))
        else:
            if element is not None:
                flatten_list.append(element)
    return flatten_list


