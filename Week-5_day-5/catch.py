def cache(func):
    memory = {}

    def wrapper(*args):
        if args in memory:
            print("Using cached value")
            return memory[args]

        result = func(*args)
        memory[args] = result
        return result

    return wrapper


@cache
def square(n):
    print("Calculating...")
    return n * n


print(square(4))
print(square(4))