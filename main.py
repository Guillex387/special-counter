import lib


def printCombinations(matrix: list, separator):
    for list in matrix:
        representation = ""
        for i in range(len(list)):
            if (i == 0):
                representation += list[i]
            else:
                representation += separator + list[i]
        print(representation)


symbols = []
digits = 0

matrix = lib.combinations(symbols, digits)

printCombinations(matrix, '')
