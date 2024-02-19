
# def function with default args
def greet(name, msg="Good morning!"):
    print("Hello", name + ', ' + msg)

greet("Kate")


# def function with arbitrary args
def greet(*names):
    for name in names:
        print("Hello", name)

greet("Monica", "Luke", "Steve", "John")


# def  function with kwargs
def greet(**kwargs):
    if kwargs:
        print("Hello", kwargs['name'], kwargs['msg'])

greet(name="Kate", msg="Good morning!")


# def final function including everyting

def final_function(arg1, arg2, *args, arg3="myarg", **kwargs):
    print("arg1: ", arg1)
    print("arg2: ", arg2)
    print("args: ", args)
    print("arg3: ", arg3)
    print("kwargs: ", kwargs)

final_function(10, 20, 30, 40, 50, arg3="myarg", key1="value1", key2="value2")


# def pass by reference
def change_list(my_list):
    print(id(my_list))
    my_list.append([1, 2, 3, 4])

my_list = [10, 20, 30]
print(id(my_list))
change_list(my_list[:])
print("Values outside the function: ", my_list)