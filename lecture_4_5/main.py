# Introduction to Boolean Values
# Loops (for and while loops)
# Loop Control Statements (break, continue)
# Functions (Defining, Calling, and Passing Arguments)

# Introduction to Boolean Values
a = False
b = True
if a:
    print("a is True")
else:
    print("a is False")



if a or b:
    print("a or b is True")
else:
    print("a and b is False")


# loops
# for loop    
arr = [1, 2, 3, 4, 5]
for i in arr:
    print(i)

for i in arr:
    if i == 3:
        continue
    print(i)

    if i == 4:
        break


# while loop
    
count = 0
while count < 5:
    print(count)
    count += 1


# else in loops
    
for num in range(10):
    if num == 5:
        break 
    print(num)
else:
    print("not break")





# functions
def my_function():
    print("Hello from a function")
my_function()

def my_function_with_args(username, greeting):
    print(f"Hello, {username}, from My Function!, I wish you {greeting}")
my_function_with_args("John Doe", "a great day")

def sum_two_numbers(a, b):
    l = [a, b]
    return l
print(sum_two_numbers(5, 7))

