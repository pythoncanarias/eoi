def abs_args(func):
    def inner_function(a, b):
        a = abs(a)
        b = abs(b)
        return func(a, b)
    return inner_function


@abs_args
def product(a, b):
    return a * b


print(product(-3, 8))
