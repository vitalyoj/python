n = input().strip()
print(f"{int(n):b}, {int(n):o}, {int(n):x}" if n.isdigit() and int(n) > 0 else "Неверный ввод")
