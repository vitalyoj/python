input_str = input()
index_comma = input_str.find(',')
s = input_str[:index_comma]
i = input_str[index_comma+1]

count = 0

for char in s:
    if char == i:
        count += 1
    else:
        break
print(count)
