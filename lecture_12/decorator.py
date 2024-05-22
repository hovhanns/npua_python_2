# def parent(num):
#     def first_child():
#         return "Hi, I'm First"
#
#     def second_child():
#         return "Call me Second"
#
#     if num == 1:
#         return first_child
#     else:
#         return second_child
#
# first = parent(1)
# second = parent(2)
# print(first())
# print(second())


# def decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening after the function is called.")
#     return wrapper
#
# def say_whee():
#     print("Whee!")
#
# say_whee = decorator(say_whee)

import functools
def do_twice(func):
    def wrapper_do_twice():
        func()
        func()
    return wrapper_do_twice

# def do_twice_args(func):
#     @functools.wraps(func)
#     def wrapper_do_twice(*args, **kwargs):
#         func(*args, **kwargs)
#         return func(*args, **kwargs)
#     return wrapper_do_twice