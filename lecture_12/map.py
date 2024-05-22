# map(function_to_apply, list_of_inputs)

items = [1, 2, 3, 4, 5, 7]
# squared = []
# for i in items:
#     squared.append(i * i)
# print(squared)
# squared = list(map(lambda x: x ** 2, items))
# print(squared)

def multiply(x):
    return (x*x)
def add(x):
    return (x+x)
def xoranard(x):
    return (x**3)

funcs = [multiply, add, xoranard]
for i in range(5):
    value = list(map(lambda x: x(i), funcs))
    print(value)