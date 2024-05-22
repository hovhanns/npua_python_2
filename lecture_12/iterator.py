list_instance = [1, 2, 3, 4]
# print(iter(list_instance))
# print(next(list_instance))

iterator = iter(list_instance)
print(iterator)
# return items one at a time
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
# for iterator in list_instance:
#   print(iterator)