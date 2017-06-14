def logged(func):
    def func_wrapper(*args, **kwargs):
        if args:
            # Printing function name and arguments
            function_call = ("You called " +
                             func.__name__ +
                             "(" + str(args[0]))

            for i in range(1, len(args)):
                function_call += ", " + str(args[i])

            function_call += ")"
            print(function_call)
        else:
            # Printing the name of the function to be logged
            print("You called " + func.__name__ + "()")

        if kwargs:
            print("Named arguments and their values:")
            # Printing kwargs
            for key, value in kwargs.iteritems():
                print(key, value)

        returned_val = func(*args, **kwargs)

        print("It returned " + str(returned_val))

        return returned_val
    return func_wrapper


@logged
def foo(*args, **kargs):
    return 3 + len(args)


if __name__ == "__main__":
    print foo(10, i=19)
