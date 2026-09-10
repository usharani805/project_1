# Simple decorator example

def my_decorator(function):
    def wrapper():
        print("Before the function")
        function()
        print("After the function")

    return wrapper


@my_decorator
def greet():
    print("Hello Python")


greet()