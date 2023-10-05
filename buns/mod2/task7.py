s = input()
count0 = 0
count1 = 0

for char in s:
    if char == '0':
        count0 += 1
    elif char == '1':
        count1 += 1

if count0 == count1:
    print('yes')
else:
    print('no')
