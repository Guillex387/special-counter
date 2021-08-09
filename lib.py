import math as __math

# Public methods


def n_combinations(n_symbols: int, n_digits: int):
    float_value = __math.pow(n_symbols, n_digits)
    return round(float_value)


def combinations(symbols: list, digits: int):
    combinations = []
    counter = []
    for i in range(digits):
        counter.append(symbols[0])
    combinations.append(counter.copy())
    for _ in range(n_combinations(len(symbols), digits) - 1):
        __increment_recursively(symbols, counter, digits - 1)
        combinations.append(counter.copy())
    return combinations

# Private methods


def __increment_recursively(symbols: list, counter: list, pos: int):
    stopIndex = len(symbols) - 1
    if counter[pos] == symbols[stopIndex]:
        counter[pos] = symbols[0]
        if pos >= 0:
            __increment_recursively(symbols, counter, pos - 1)
        return
    counter[pos] = __nextLocation(symbols, counter[pos])


def __nextLocation(symbols: list, actual):
    target_iteration = False
    for symbol in symbols:
        if target_iteration:
            return symbol
        if symbol == actual:
            target_iteration = True
    if target_iteration:
        return symbols[0]
    return False
