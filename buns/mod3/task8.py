input_number = input();
cleaned_number = ''.join(ch for ch in input_number if ch.isdigit() or ch == '+')
print(cleaned_number)
