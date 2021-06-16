n = 0
board = [[0] * 100] * 100
cache = [[-1] * 100] * 100
def jump2(y,x):
    if y>=n or x>=n:
        return 0
    if y== n-1 and x== n-1:
        return 1
    ret = cache[y][x]
    if ret != -1:
        return ret
    jump_size = board[y][x]
    return jump2(y + jump_size, x) or jump2(y, x + jump_size)

    