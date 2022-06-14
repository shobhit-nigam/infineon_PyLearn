# define a function
# variable number of arguments
# args kwargs

def greet(la, lb, *args, **kwargs):
    print("la =", la)
    print("lb =", lb)
    print("args =", args)
    print("kwargs =", kwargs)

#
#def greet(la, lb, *args):
#    print("la =", la)
#    print("lb =", lb)
#    print("args =", args)
