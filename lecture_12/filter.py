number_list = range(-6, 5)
less_than_zero = list(filter(lambda x: x % 2==0, number_list))
print(less_than_zero)