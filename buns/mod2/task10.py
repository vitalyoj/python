input_string = input()
new_word = ""

for i in range(len(input_string)):
    if input_string[i] == ' ' or i == len(input_string) - 1:
        if i == len(input_string) - 1 and input_string[i] != ' ':
            new_word += input_string[i]
        else:
            new_word += input_string[i-1]
print(new_word)
