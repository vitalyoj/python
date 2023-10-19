numbers = [int(x) for x in input("Введите числа через пробел: ").split()]
unique_numbers = set(numbers)
if len(unique_numbers) == 1:
    print("Все числа равны")
elif len(unique_numbers) == len(numbers):
    print("Все числа разные")
else:
    print("Есть равные и неравные числа")
