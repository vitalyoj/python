s = input()
glasnye = 'аеёиоуыэюя'
soglasnye = 'бвгджзйклмнпрстфхцчшщ'
count_glasnye = 0
count_soglasnye = 0

for char in s:
    if char in glasnye:
        count_glasnye += 1
    elif char in soglasnye:
        count_soglasnye += 1
print(count_glasnye, count_soglasnye)
