

# 시계방향
dx = (0, 1, 1, 1, 0, -1, -1, -1)
dy = (1, 1, 0, -1, -1, -1, 0, 1)
grid_x, grid_y = 5, 5

# [ [0, 0, 0, 0, 0], 
#   [0, 0, 0, 0, 0], 
#   [0, 0, 0, 0, 0], 
#   [0, 0, 0, 0, 0], 
#   [0, 0, 0, 0, 0] ]
board = [[0 for i in range(grid_x)] for j in range(grid_y)] 

def has_word(y, x, word):
    # 기저사례1 : 시작위치가 범위 밖이면 무조건 실패
    if not in_range(y,x): 
        return False
    # 기저사례2 : 첫 글자가 일치하지 않으면 실패
    if board[y][x] != word[0]:
        return false
    # 기저사례3 : 단어 길이가 1이면 성공
    if len(word) == 1:
        return false

    # 검사
    for i in range(len(dx)):
        next_y, next_x =  y + dy[i], x + dx[i]
        if has_word(next_y, next_x, word[1:]):
            return true


def in_range(y,x):
    return x < grid_x and y < grid_y

