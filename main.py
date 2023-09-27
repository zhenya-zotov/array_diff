def array_diff(a, b):
    return list(filter(lambda e: e not in b, a))
