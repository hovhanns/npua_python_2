def f():
    print("hello")

a = [[1, 2, 3],
     [2, 4, 6],
     [134, 235, 23]]
s = 0
for i, row in enumerate(a):
    for j, el in enumerate(row):
        #print(i, j, el)
        pass

a = [10, 20, 30]

for a, b in enumerate(a):
    print(a, b)



a, b = (10, 20)




import random

f = random.random()
i = random.randint(1, 10)
# get float number between 1 and 10
f = random.uniform(1, 10)
print(f)


a = 10
l = []
for i in range(10):
    l.append(random.randint(1, 10))

print(l)