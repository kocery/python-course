import functools
import warnings
from typing import Optional, Callable, Any, Union


def deprecated(
        func: Optional[Callable] = None,
        *,
        since: Optional[str] = None,
        will_be_removed: Optional[str] = None
) -> Union[Callable, Callable[[Callable], Callable]]:
    """
    Декоратор для пометки функции как устаревшей.

    Можно использовать как с аргументами:
        @deprecated(since="1.0", will_be_removed="2.0")
        def func(...):
            ...

    Так и без аргументов:
        @deprecated
        def func(...):
            ...
    """

    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            message = f"Warning: function {func.__name__} is deprecated"
            if since:
                message += f" since version {since}."
            else:
                message += "."

            if will_be_removed:
                message += f" It will be removed in version {will_be_removed}."
            else:
                message += " It may be removed in future versions."

            # Используем warnings.warn вместо print для лучшей интеграции с системой предупреждений Python
            warnings.warn(message, DeprecationWarning, stacklevel=2)
            return func(*args, **kwargs)

        return wrapper

    if func is not None and callable(func):
        # Декоратор используется без аргументов
        return decorator(func)
    else:
        # Декоратор используется с аргументами
        return decorator


# Примеры использования

@deprecated(since="1.0", will_be_removed="2.0")
def old_function():
    print("This is an old function.")


@deprecated(since="1.0")
def older_function():
    print("This function is a bit older.")


@deprecated(will_be_removed="2.0")
def oldest_function():
    print("This function is the oldest.")


@deprecated
def legacy_function():
    print("Legacy function with no specified version.")


@deprecated
def baz(x, y):
    return x * y


if __name__ == "__main__":
    old_function()
    older_function()
    oldest_function()
    legacy_function()
    result = baz(3, 4)
    print(f"Result of baz(3, 4): {result}")
