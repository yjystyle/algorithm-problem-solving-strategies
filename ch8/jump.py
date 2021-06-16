n = 100
board = [[0] * 100] * 100


def jump(y, x) -> bool:
    if y >= n or x >= n:
        return False
    if y == n-1 and x == n-1:
        return True
    jump_size = board[y][x]
    return jump(y + jump_size, x) or jump(y, x + jump_size)
