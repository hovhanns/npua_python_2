# reading and writitng files
f = open("file.txt", "w")
f.write("Hello World")
f.close()

f = open("file.txt", "r")
s = f.read()
print(s)
f.close()


# reading file lines
f = open("file.txt", "r")
l = f.readlines()
print(l)
f.close()

try:
    l = []
    print(l[10])
except IndexError as e:
    print("Index out of range")
else:
    print("No exception")
finally:
    print("Always executed")


