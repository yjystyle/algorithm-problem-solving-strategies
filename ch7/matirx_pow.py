def identity(n):
    m = [[0 for x in range(n)] for y in range(n)]
    for i in range(0, n):
        m[i][i] = 1
    return m


def pow(A: list, m: int) -> list:
    if m == 0:
        return identity(len(m))
    if m == 1:
        return A
    if m % 2 > 0:
        return pow(A, m-1) * A
    return pow(A, m/2) * pow(A, m/2)

print(pow(identity(5), 25))
