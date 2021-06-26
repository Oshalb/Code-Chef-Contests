# Tic Tac Toe

def play_game(r, c, k):
    board = [['0' for i in range(c)]for j in range(r)]
    a = [['A' for i in range(k)]for j in range(k)]
    t = 0
    for k in range(r*c):
        i, j = map(int, input().rstrip().split())
        i -= 1
        j -= 1
        if t == 0:
            board[i][j] = 'A'
            t += 1
        else:
            board[i][j] = 'B'
            t -= 1
        for x in range(r):
            for y in range(c):
                pass
    if a in board:
        print(board, sep="\n")
    return 0


if __name__ == "__main__":
    number_of_testcases = int(input())
    for _ in range(number_of_testcases):
        rows_of_board, column_of_board, grid_to_win = map(int, input().rstrip().split())
        result = play_game(rows_of_board, column_of_board, grid_to_win)
