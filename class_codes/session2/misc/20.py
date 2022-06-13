
print("hello world")

display = print

display("hello world")

# becomes an int
print = 10

# local defintion is deleted 
del print
# print = __builtins__.print

print("hey")

print = __builtins__.print
