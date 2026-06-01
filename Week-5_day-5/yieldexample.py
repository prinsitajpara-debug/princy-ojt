def generate_numbers(n):
    for i in range(1, n + 1):
        yield i

gen = generate_numbers(5)

print(next(gen))  
print(next(gen))  
print(next(gen))  
print(next(gen))  
print(next(gen))  


#using loop
def squares():
    for i in range(1, 6):
        yield i * i

for value in squares():
    print(value)


#using loop yield1,yield2
def numbers():
    yield 1
    yield 2

for value in numbers():
    print(value)
