def solve_n_rooks(n):
    board = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        board[i][i] = 1  
    for row in board:
        print(' '.join(str(cell) for cell in row))

n = int(input("Enter the value of N: "))
solve_n_rooks(n)
