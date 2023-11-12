import time
def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Время выполнения {func.__name__}: {end_time - start_time} секунд")
        return result
    return wrapper

def memoize(func):
    cache = {}

    def wrapper(*args):
        if args not in cache:
            result = func(*args)
            cache[args] = result
        return cache[args]

    wrapper.__name__ = func.__name__
    wrapper.__doc__ = func.__doc__

    return wrapper

@timer
@memoize
def fibonacci_memoize(n):
    if n < 2:
        return n
    return fibonacci_memoize(n - 1) + fibonacci_memoize(n - 2)

@timer
def fibonacci_original(n):
    if n < 2:
        return n
    return fibonacci_original(n - 1) + fibonacci_original(n - 2)

# время выполнения
n = 35

print("Сравнение времени выполнения без memoize:")
fibonacci_original(n)

print("\nСравнение времени выполнения с memoize:")
fibonacci_memoize(n)
