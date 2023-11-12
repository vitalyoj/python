def memoize(func):
    cache = {}
    names = func.__code__.co_varnames
    docstring = func.__doc__

    @wraps(func)
    def wrapper(*args, **kwargs):
        key = (args, frozenset(kwargs.items()))
        if key not in cache:
            result = func(*args, **kwargs)
            cache[key] = result
        return cache[key]

    # сохранение имени и строки документации
    wrapper.__orig_name__ = func.__name__
    wrapper.__doc__ = docstring

    return wrapper

@memoize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

result = fibonacci(10)
print(result)
