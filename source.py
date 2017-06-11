import sys

def logged(func):
    def func_wrapper(*args, **kwargs):
        if(len(args)!=0):
            # Printing function name and arguments
            sys.stdout.write("You called "
                             + func.__name__
                             + "("
                             + str(args[0]))
            # Traversing over the args to print them
            # --------------------------------------
            for i in range(1,len(args)):
                sys.stdout.write(", " + str(args[i]))
            print (")")
            sys.stdout.flush()
            # --------------------------------------
        else:
            # Printing the name of the function to be logged
            print ("You called " + func.__name__ + "()")
        # Printing the return value by the func
        print ("It returned " + str(func(*args, **kwargs)))

        return func(*args, **kwargs)
    return func_wrapper

@logged
def foo(*args):
    return 3 + len(args)

if __name__ == "__main__":
    print foo(4, 8, 9)
