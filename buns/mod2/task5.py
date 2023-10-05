alphabet = 'abcdefghijklmnopqrstuvwxyz'
i, n = input().split(',')
n = int(n)
index = alphabet.index(i)
new_index = (index + n) % 26
print(alphabet[new_index])
