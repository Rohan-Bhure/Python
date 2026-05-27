# A decorator is used to:
# modify behavior of a function
# add extra functionality
# without changing original function code

from functools import wraps
# @wraps(func) -> presevese the __name__,anotaiton, docstring etc, module other wise it will give wrapper relate things
# Functions are First-Class Objects in Python
# Python treats functions like variables.
# You can:
# store function in variable
# pass function as argument
# return function from another function

from functools import wraps


# -------------------------------------------------
# 1) Function inside function
# -------------------------------------------------
def outer():
    def inner():
        print("Hello from inner")
    return inner


x = outer()
x()   # Hello from inner


# -------------------------------------------------
# 2) Basic decorator
# -------------------------------------------------
def decorator_function(original_function):
    @wraps(original_function)
    def wrapper():
        print("Extra work before function")
        original_function()
        print("Extra work after function")
    return wrapper


@decorator_function
def greet():
    print("Hello")


greet()


# -------------------------------------------------
# 3) Logger decorator
# -------------------------------------------------
def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Function {func.__name__} started")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} ended")
        return result
    return wrapper


@logger
def say_hello():
    print("Hello")


say_hello()


# -------------------------------------------------
# 4) Game handler decorator
# -------------------------------------------------
def game_handler(func):
    @wraps(func)
    def wrapper():
        print("Game started")
        func()
        print("Game ended")
    return wrapper


@game_handler
def game():
    print("Game is running")


game()


# If you want to call the decorated function through x:
x = game_handler(game.__wrapped__)   # original undecorated game
x()


# -------------------------------------------------
# 5) Flexible decorator
# -------------------------------------------------
def extra_info(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Arguments:", args)
        print("Keyword arguments:", kwargs)
        return func(*args, **kwargs)
    return wrapper


@extra_info
def add(*args):
    return sum(args)


result = add(2, 5, 4, 4)
print(result)


# -------------------------------------------------
# 6) Function call counter
# -------------------------------------------------
def func_counter(func):
    counter = 0

    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal counter
        counter += 1
        print(f"{func.__name__} is called for {counter} time(s)")
        return func(*args, **kwargs)
    return wrapper


@func_counter
def caller():
    print("I am caller function")


caller()
caller()
caller()


# -------------------------------------------------
# 7) Logs function name, args, kwargs, and return value
# -------------------------------------------------
def logs(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Function name:", func.__name__)
        print("Arguments:", args)
        print("Keyword arguments:", kwargs)

        result = func(*args, **kwargs)

        print("Returned value:", result)
        return result
    return wrapper


@logs
def sum_numbers(*args, **kwargs):
    return sum(args)


x = sum_numbers(1, 4, 4, 5)
print(x)


# -------------------------------------------------
# 8) Parameterized decorator repeat(n)
# -------------------------------------------------
def repeat(n):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(n):
                print(f"Run {i + 1}")
                func(*args, **kwargs)
        return wrapper
    return decorator


@repeat(4)
def func1():
    print("func1 is printed")


func1()


# -------------------------------------------------
# 9) Access control decorator
# -------------------------------------------------
def access_checker(role):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if role in ("admin", "editor"):
                print("Access allowed")
                return func(*args, **kwargs)
            else:
                print("Access denied")
        return wrapper
    return decorator


@access_checker(role="user")
def company_info():
    print("Company data is here...")


company_info()


# -------------------------------------------------
# 10) Stacking decorators
# -------------------------------------------------
def decorator_one(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Decorator One: Before")
        result = func(*args, **kwargs)
        print("Decorator One: After")
        return result
    return wrapper


def decorator_two(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Decorator Two: Before")
        result = func(*args, **kwargs)
        print("Decorator Two: After")
        return result
    return wrapper


@decorator_one
@decorator_two
def show():
    """This is show function"""
    print("Inside function")


show()
print(show.__name__)
print(show.__doc__)


# -------------------------------------------------
# 11) Input validation decorator
# -------------------------------------------------
def validate_input(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not args:
            print("Invalid Input")
            return

        for value in args:
            if not isinstance(value, (int, float)):
                print("Invalid Input")
                return

        return func(*args, **kwargs)
    return wrapper


@validate_input
def multiply(a, b):
    return a * b


print(multiply(5, 3))
print(multiply(5, "3"))