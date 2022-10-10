#Check that a tuple cannot be changed in python
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "orange"
x = tuple(y)

print(x)