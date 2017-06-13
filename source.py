import sys


def logged(func):
    def func_wrapper(*args, **kwargs):
        if len(args) != 0:
            # Printing function name and arguments
            sys.stdout.write("You called " +
                             func.__name__ +
                             "(" + str(args[0]))
            # Traversing over the args to print them
            # --------------------------------------
            for i in range(1, len(args)):
                sys.stdout.write(", " + str(args[i]))
            print(")")
            sys.stdout.flush()
            # --------------------------------------
        else:
            # Printing the name of the function to be logged
            print("You called " + func.__name__ + "()")

        # Printing named args
        if len(kwargs) > 0:
            print("Named arguments and their values:")
            # Printing kwargs
            for key, value in kwargs.iteritems():
                print(key, value)
        else:
            print("No named arguments passed")

        return_val = func(*args, **kwargs)
        # Printing the return value by the func
        print("It returned " + str(return_val))

        return return_val
    return func_wrapper


@logged
def foo(*args, **kargs):
    return 3 + len(args)

if __name__ == "__main__":
    print foo(4)
