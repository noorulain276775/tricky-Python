def create_funcs():
    """
    Late Binding in Python Lambdas

    This function demonstrates the late binding behavior of Python closures
    when using lambdas inside loops.

    The lambdas capture the variable 'i' itself, not its value at the time 
    of the lambda's creation. Therefore, when the lambdas are called later,
    they all return the final value of 'i' after the loop ends.

    Example:
        funcs = create_funcs()
        results = [f() for f in funcs]
        print(results)  # Output: [2, 2, 2]

    To fix this issue, use default arguments in the lambda to bind the current
    value of 'i' at definition time:

        funcs = [lambda i=i: i for i in range(3)]
        results = [f() for f in funcs]
        print(results)  # Output: [0, 1, 2]
    """
    funcs = []
    for i in range(3):
        funcs.append(lambda: i)
    return funcs

