# Читаем строку
input_str = input()

try:
    num = int(input_str)

    # Проверка на натуральное число
    if num <= 0:
        raise ValueError

    # Преобразование в двоичную систему
    temp = num
    binary_repr = ""
    while temp > 0:
        binary_repr = str(temp % 2) + binary_repr
        temp //= 2

    # Преобразование в восьмеричную систему
    temp = num
    octal_repr = ""
    while temp > 0:
        octal_repr = str(temp % 8) + octal_repr
        temp //= 8

    # Преобразование в шестнадцатеричную систему
    temp = num
    hex_repr = ""
    hex_digits = "0123456789ABCDEF"
    while temp > 0:
        hex_repr = hex_digits[temp % 16] + hex_repr
        temp //= 16

    print(f"{binary_repr}, {octal_repr}, {hex_repr}")

except ValueError:
    print("Неверный ввод")
