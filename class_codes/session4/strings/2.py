
name = "john doe"
age = 41
val = 56.893674987

print("name is", name, "and age is", age)

# basic formatting (older, c style)
print("name is %s and age is %d" %(name, age))

# basic formatting (older, format function)
print("name is {} and age is {}".format(name, age))

# basic formatting (older, format function)
print("name is {0} and age is {1}, remember name is {0}".format(name, age))

# basic formatting (older, format function)
print("val is {:.4f}".format(val))
