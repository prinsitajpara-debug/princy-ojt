items = ["A", "B", "C", "D"]

it = iter(items)

print(next(it))  # A
print(next(it))  # B
print(next(it))  # C

# we stop here manually, so we DON'T call next(it) 4th time