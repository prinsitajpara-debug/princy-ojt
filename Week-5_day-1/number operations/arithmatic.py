def arithmatic(a, b):
    """Perform basic arithmatic operations on two numbers"""
    return{
        "multiply": a * b,
        "divide": a / b,
        "add": a + b,
        "subtract": a - b,
        "modulo": a % b,
        "floor_divide": a // b
    }

print(arithmatic(6, 2))
