'''
Ref: https://www.geeksforgeeks.org/the-knights-tour-problem-backtracking-1/
'''

# move_x and move_y define next move of Knight.
# move_x is for next value of x coordinate
# move_y is for next value of y coordinate
'''
Represents moves in order:

  x     x       xx      xxx
  xxx   x       x         x
        xx      x
  
'''
move_x = [2, 1, -1, -2, -2, -1, 1, 2]
move_y = [1, 2, 2, 1, -1, -2, -2, -1]


def is_safe(x, y, n, board):
    '''
    Check if (x, y) is a valid position on a n-sized board
    Args:
        x (int): x coordinate
        y (int): y coordinate
        n (int): board size
        board (list): 2D integer list denoting\
            current state of board
    '''
    if x < 0 or x >= n:
        return False

    if y < 0 or y >= n:
        return False

    if board[x][y] != -1:
        # if its anything other than what we
        # explicitly inited with -1
        return False

    # safe to return True now
    return True


def print_board(n, board):
    '''
    Couple of nested for loops to print the board
    Args:
        n (int): board size
        board (list): 2D integer list denoting\
            current state of board
    '''
    for x in range(n):
        for y in range(n):
            _print_this = board[x][y] if board[x][y] > 9 else f' {board[x][y]}'
            print(_print_this, end=' ')
        print()


def main(n):

    # init board
    board = [[-1 for _ in range(n)] for _ in range(n)]
    '''
    [
        [-1, -1, -1, -1, -1, -1, -1, -1],
        ... 8
    ]
    '''

    # since the knight starts at the first square
    curr_x = 0
    curr_y = 0

    # placing knight on board by marking it as 0
    board[curr_x][curr_y] = 0

    # step ctr for knight's position
    # this will be in the range 1 to n**2
    pos = 1

    if solve_knights_tour(n, board, curr_x, curr_y, pos):
        print_board(n, board)


def solve_knights_tour(n, board, curr_x, curr_y, pos):
    '''
    Recursive
    '''
    # if managed to reach end that means
    # all squares have been visited
    # this is the stop condition
    if pos == n**2:
        return True

    # iterate over possible moves
    for i in range(8):  # max 8 moves for any given position

        # setting new coordinates to check
        new_x = curr_x + move_x[i]
        new_y = curr_y + move_y[i]

        # check for safety first
        if not is_safe(new_x, new_y, n, board):
            continue

        # set current pos on board at new coordinates
        board[new_x][new_y] = pos

        # recurse to solve the rest by passing the next position
        if solve_knights_tour(n, board, new_x, new_y, pos=pos+1):
            return True

        # Backtracking:
        # setting the board to be -1 on new coordinates
        board[new_x][new_y] = -1

    # if all of the above fails
    return False


if __name__ == '__main__':
    n = 8  # WARNING: integers greater than 8 DO NOT scale well
    main(n)
