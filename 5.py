def sum(x, y):
    return x, y


def specialize(fun, *args, **kwargs):
    def f(*extra_args, **extra_kwargs):
        return fun(*args, *extra_args, **kwargs, **extra_kwargs)

    return f


plus_one = specialize(sum, y=1)
just_two = specialize(sum, 1, 1)

print(plus_one(10))
print(just_two())
