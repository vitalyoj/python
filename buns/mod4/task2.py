def fast_power(a, n):
    if n == 0:
        return 1
    if n % 2 == 0:
        return fast_power(a * a, n // 2)
    else:
        return a * fast_power(a, n - 1)
a = 2
n = 10
result = fast_power(a, n)
print(f"{a}^{n} = {result}")
