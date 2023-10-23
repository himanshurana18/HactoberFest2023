def solve_n_queens(n):
    def is_valid(board, row, col):
        for i in range(row):
            if board[i] == col or \
                board[i] - i == col - row or \
                board[i] + i == col + row:
                return False
        return True

    def backtrack(board, row):
        if row == n:
            result.append(board[:])
            return

        for col in range(n):
            if is_valid(board, row, col):
                board[row] = col
                backtrack(board, row + 1)
                board[row] = -1

    result = []
    board = [-1] * n
    backtrack(board, 0)

    # Convert to visual representation
    output = []
    for res in result:
        output.append(["." * i + "Q" + "." * (n - i - 1) for i in res])
    return output

# For example
for solution in solve_n_queens(4):
    for row in solution:
        print(row)
    print("\n")
