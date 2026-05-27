from mypackage import add, divide, to_upper, reverse, write_file, read_file
from mypackage.config import Config

print("App Name:", Config.APP_NAME)

print(add(10, 5))
print(divide(10, 0))

print(to_upper("hello"))
print(reverse("python"))

print(write_file("test.txt", "Hello World"))
print(read_file("test.txt"))