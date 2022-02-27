# sort by key
def sort_dict(d: dict):
    keys = sorted(d.keys())
    new_d = {}
    # going over values after sorting keys
    for key in keys:
        if isinstance(d[key], list):
            new_d[key] = sorted(d[key])
        elif isinstance(d[key], dict):
            # recursive call
            new_d[key] = sort_dict(d[key])
        elif isinstance(d[key], set):
            new_d[key] = set(sorted(d[key]))
        elif isinstance(d[key], tuple):
            new_d[key] = tuple(sorted(d[key]))
        else:
            new_d[key] = d[key]
    return new_d


def sort(t):
    new = []
    composite = []
    for var in t:
        # recursive call
        if isinstance(var, list) or isinstance(var, set) or isinstance(var, tuple):
            composite.append(sort(var))
        elif isinstance(var, dict):
            composite.append(sort_dict(var))
        else:
            new.append(var)
    # appending composites to the end of the list
    if len(composite) != 0:
        new = sorted(new)
        for var in composite:
            new.append(var)
        return new
    else:
        return sorted(new)


# sort function returns a list, this function will cast the return value to the the correct type / calls sort_dict
def print_sorted(x):
    if isinstance(x, list):
        sort(x)
    elif isinstance(x, dict):
        x = sort_dict(x)
    elif isinstance(x, set):
        x = set(sort(x))
    elif isinstance(x, tuple):
        x = tuple(sort(x))
    print(x)
    return x


if __name__ == '__main__':
    print_sorted({1: {5: 0, 4: 2}, 8: {1: (1, 7, 3), 0: [5, 0, -9]}, 2: (5, 7, 4, 1), 13: {"2": "a", "1": "0"}})
    print_sorted({"d": {7, 4, 3, -2}, "a": "hi", "b": [6, 5, 1]})
    # doesn't work
    print_sorted((3, [4, 3, 2], 1))
