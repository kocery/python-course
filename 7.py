import functools


def deprecated(since=None, will_be_removed=None):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if since and will_be_removed:
                print(
                    f"Warning: function {func.__name__} is deprecated since version {since}. It will be removed in version {will_be_removed}")
            elif since:
                print(
                    f"Warning: function {func.__name__} is deprecated since version {since}. It will be removed in future versions")
            elif will_be_removed:
                print(
                    f"Warning: function {func.__name__} is deprecated. It will be removed in version {will_be_removed}")
            else:
                print(f"Warning: function {func.__name__} is deprecated and may be removed in future versions")
            return func(*args, **kwargs)

        return wrapper

    return decorator


@deprecated(since="1.0", will_be_removed="2.0")
def old_function():
    print("This is an old function.")


@deprecated(since="1.0")
def older_function():
    print("This function is a bit older.")


@deprecated(will_be_removed="2.0")
def oldest_function():
    print("This function is the oldest.")


@deprecated()
def legacy_function():
    print("Legacy function with no specified version.")


old_function()
older_function()
oldest_function()
legacy_function()
