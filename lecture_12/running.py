# from decorator import do_twice
# from decorator import do_twice_args
# from timer_decorator import timer
# @do_twice
# def say_whee():
#     print("Whee!")
#
# say_whee()
#
# @do_twice_args
# def say_hey(name):
#     print(f"Hello {name}")
#
# @timer
# def time(name):
#     print(f"Hello {name}")
#
# time("Bob")
# # say_hey("Bob")
# #
# # help(say_hey)
# # print(say_whee.__name__)
# # print(say_whee.__doc__)
#
from timer_decorator import timer
@timer
def running():
    sum = 0;
    for i in range(1000):
        sum=i+sum
        # print(i)
    # print(sum)

@timer
def map1():
    list =map(lambda x:x+1,range(100000))

    for e in list:
        print()

# running()
map1()
from dis import dis
dis(map1)
dis(running)