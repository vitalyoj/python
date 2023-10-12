lines = []
k = 3  
for i in range(k):
    line = input()
    lines.append(line)

for line in lines:
    if 'X' * k in line:
        print("X")
        exit()
    elif 'O' * k in line:
        print("O")
        exit()

for col in range(k):
    column = ''.join([lines[row][col] for row in range(k)])
    if 'X' * k in column:
        print("X")
        exit()
    elif 'O' * k in column:
        print("O")
        exit()

diag1 = ''.join([lines[i][i] for i in range(k)])
diag2 = ''.join([lines[i][k-i-1] for i in range(k)])

if 'X' * k in diag1 or 'X' * k in diag2:
    print("X")
    exit()
elif 'O' * k in diag1 or 'O' * k in diag2:
    print("O")
    exit()

print("Ничья")
