# Define a generator function
def countdown(n):
    while n > 0:
        yield n
        n -= 1

# Create an iterator from the generator
iterator = countdown(5)

# Iterate over the values using a for loop
for value in iterator:
    print(value)

# Output: 5, 4, 3, 2, 1

# Use the next() function to get the next value from the iterator
print(next(iterator))  # Output: 5
print(next(iterator))  # Output: 4

# Use the iter() function to create a new iterator from the iterable
new_iterator = iter([1, 2, 3, 4, 5])

# Iterate over the values using a for loop
for value in new_iterator:
    print(value)
# Output: 1, 2, 3, 4, 5

# Create a list
my_list = [1, 2, 3, 4, 5]
# Iterate over the values using a for loop
for value in my_list:
    print(value)
# Output: 1, 2, 3, 4, 5

# Create a generator
my_generator = (x for x in range(1, 6))
# Iterate over the values using a for loop
for value in my_generator:
    print(value)
# Output: 1, 2, 3, 4, 5

