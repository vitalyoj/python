def can_form_palindrome(s):
    char_counts = {}
    for char in s:
        char_counts[char] = char_counts.get(char, 0) + 1

    odd_chars = [char for char, count in char_counts.items() if count % 2 == 1]


    if len(odd_chars) > 1:
        return False, None

    middle = odd_chars[0] if odd_chars else ""
    half_palindrome = "".join([char * (count // 2) for char, count in char_counts.items()])

    palindrome = half_palindrome + middle + half_palindrome[::-1]

    return True, palindrome

word = input("Введите слово: ")
possible, palindrome = can_form_palindrome(word)
if possible:
    print("Палиндром:", palindrome)
else:
    print("Нельзя составить палиндром.")
