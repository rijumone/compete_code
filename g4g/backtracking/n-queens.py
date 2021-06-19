'''
Place N queens on an N*N chessboard such
that all queens are safe.

Ref: https://www.geeksforgeeks.org/n-queen-problem-backtracking-3/
'''


def is_safe(x, y, n, board) -> bool:
    '''
    Check if (x, y) is a valid position on a n-sized board
    Args:
        x (int): x coordinate
        y (int): y coordinate
        n (int): board size
        board (list): 2D integer list denoting\
            current state of board
    Returns:
        bool
    '''
    if x < 0 or x >= n:
        return False

    if y < 0 or y >= n:
        return False

    if board[x][y] == 'X':
        # a queen is already placed there
        return False

    if 'X' in board[x]:
        # if there is another queen in the same row
        return False

    for row in board:
        for i, square in enumerate(row):
            if i != y:
                continue
            if square == 'X':
                # if there is another queen in the same column
                return False

    # Slow-n-Dirty check for diagonals
    i, j = x, y
    while True:
        try:
            if board[i+1][j+1] == 'X':
                return False
            i += 1
            j += 1
        except IndexError:
            break

    i, j = x, y
    while True:
        try:
            if board[i-1][j-1] == 'X':
                return False
            i += 1
            j += 1
        except IndexError:
            break

    i, j = x, y
    while True:
        try:
            if board[i-1][j+1] == 'X':
                return False
            i += 1
            j += 1
        except IndexError:
            break

    i, j = x, y
    while True:
        try:
            if board[i+1][j-1] == 'X':
                return False
            i += 1
            j += 1
        except IndexError:
            break

    return True


def print_board(board):
    '''
    Couple of nested for loops to print the board
    Args:
        board (list): 2D integer list denoting\
            current state of board
    '''
    for row in board:
        for square in row:
            print(square, end=' ')
        print()

    # print('==================')


def main(n):

    # init board
    board = [['-' for _ in range(n)] for _ in range(n)]

    # board[1][1] = 'X'
    # print_board(board)
    # print(is_safe(0, 2, n, board))
    # return

    # since the first queen is placed in the first square
    queen_n = 0  # has to go up to n
    curr_x = 0
    curr_y = 0

    # placing queen on board by marking it as 'X'
    board[curr_x][curr_y] = 'X'

    # step ctr for first queen's position
    # this will be in the range 1 to n**2
    pos = 1

    if solve_n_queens(n, board, curr_x, curr_y, pos, queen_n):
        print_board(n, board)


def solve_n_queens(n, board, curr_x, curr_y, pos, queen_n):
    '''
    Recursive
    '''
    # if managed to reach end that means
    # all squares have been visited.
    # This is the stop condition
    # if pos == n**2:
    #     return True

    # if ran out of queens
    # This is another stop condition
    if queen_n >= n:
        return True
    new_x, new_y = curr_y, curr_y
    # Does this have to be an infinite loop?
    while pos < n**2:
        pos += 1
        # print(pos, n**2)
        new_x = new_x+1 if new_x < (n-1) else 0
        new_y = new_y+1 if new_y < (n-1) else 0

        # check for safety first
        if not is_safe(new_x, new_y, n, board):
            continue

        # set a queen at new coordinates
        board[new_x][new_y] = 'X'

        # increment n_queen
        queen_n += 1

        print_board(board)

        if solve_n_queens(n, board, new_x, new_y, pos, queen_n):
            return True

        # Backtracking
        board[new_x][new_y] = 'X'
        queen_n -= 1

    return False


if __name__ == '__main__':
    n = 5
    main(n)
