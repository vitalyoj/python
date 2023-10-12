numbers = input().split()
result = any(numbers.count(x) > 1 for x in numbers)
print(result)
