def add(a, b):
    try:
        return a + b
    except TypeError:
        return "Error: invalid input types"

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: cannot divide by zero"
    except TypeError:
        return "Error: invalid input types"