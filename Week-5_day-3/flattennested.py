from itertools import chain

nested = [[1, 2], [3, 4], [5, 6]]

flat = list(chain.from_iterable(nested))

print(flat)