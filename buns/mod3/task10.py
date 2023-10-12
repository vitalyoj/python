def generate_matrix(size):
    return [[i + 1 for i in range(size)] for _ in range(size)]

def transpose_on_place(matrix):
    size = len(matrix)
    for i in range(size):
        for j in range(i + 1, size):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

def print_matrix(matrix):
    for row in matrix:
        print(", ".join(map(str, row)))
    print()

def main():
    size = int(input())
    matrix = generate_matrix(size)

    print_matrix(matrix)

    transpose_on_place(matrix)

    print_matrix(matrix)

if __name__ == "__main__":
    main()
