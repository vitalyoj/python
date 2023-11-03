def armstrong_number(n):
    digits = [int(digit) for digit in str(n)]
    power = len(digits)
    return n == sum([digit ** power for digit in digits])

def armstrong_numbers_generator():
    n = 10  # с 10
    while True:
        if armstrong_number(n):
            yield n
        n += 1

gen = armstrong_numbers_generator()

for i in range(8):
    print(next(gen), end=' ')
