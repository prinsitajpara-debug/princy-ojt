items = ["A", "B", "C", "D"]

it = iter(items)

while True:
    try:
        print(next(it))
    except StopIteration:
        break