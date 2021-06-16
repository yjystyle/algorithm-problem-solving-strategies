# 6-7
n = 7
path = []
dist = [[0]*n]*n
visited = [0] * n
currentLength = 0
def shortestPath (path, visited, currentLength):
    if len(path) == n:
        return currentLength + dist[path[0]][path[-1]]
    ret = 9999999999
    for _next in range (n):
        if visited[_next] == 1:
            continue
        here = path[-1]
        path.append(_next)
        visited[next] = 1
        cand = shortestPath(path, visited, currentLength + dist[here][next])
        ret = min(ret, cand)
        visited[_next] = 0
        path.pop()
    return ret

shortestPath(path, visited, currentLength)